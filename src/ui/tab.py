from dearpygui import core, simple
from services.workout import workout_services
from services.record import record_services
from services.user import user_services
from ui.chart import pie_chart, line_chart
from config import EXAMPLE_IMAGE_FILE_PATH
import requests


class Tab:
    def __init__(self, tab_name, tab_parent):
        self.tab_name = tab_name
        self.tab_parent = tab_parent
        self._composed_workout = None
        self._records = None
        self._username = None

    def compose_workout(self):
        equipment_val = core.get_value("Equipment##widget")
        exercise_type_val = core.get_value("Exercise Type##widget")
        muscle_group_val = core.get_value("Muscle Group##widget")
        if not equipment_val or not exercise_type_val or not muscle_group_val:
            simple.show_item("Fill all the inputs, please.")
        else:
            simple.hide_item("workout_composition_group")
            self._composed_workout = workout_services.get_composed_workout(
                equipment_val, exercise_type_val, muscle_group_val
            )
            core.add_group(name="buttons", parent="workout_execution_group")
            core.add_table(
                "workout_table",
                ["Exercise", "Sets", "Reps", "Example"],
                parent="workout_execution_group",
                callback=self.toggle,
            )
            for workout in self._composed_workout:
                core.add_row("workout_table", list(workout.values()))
            core.add_button(
                "Cancel##widget", callback=self.cancel_workout, parent="buttons"
            )
            core.add_button(
                "Clear##widget", callback=self.clear_table, parent="buttons"
            )
            core.add_button(
                "Save##widget", callback=self.save_workout, parent="buttons"
            )

    def generate(self):
        self._username = user_services.get_current_user().username
        with simple.tab(name=self.tab_name, parent=self.tab_parent):
            if self.tab_name == "Workout":
                core.add_spacing(count=10)
                core.add_group(name="workout_execution_group")
                core.add_group(name="workout_composition_group")
                core.add_combo(
                    "Equipment##widget",
                    items=workout_services.get_criterias_by_name("Equipment"),
                    parent="workout_composition_group",
                )
                core.add_spacing(count=4, parent="workout_composition_group")
                core.add_combo(
                    "Exercise Type##widget",
                    items=workout_services.get_criterias_by_name("Exercise Type"),
                    parent="workout_composition_group",
                )
                core.add_spacing(count=4, parent="workout_composition_group")
                core.add_combo(
                    "Muscle Group##widget",
                    items=workout_services.get_criterias_by_name("Major Muscle"),
                    parent="workout_composition_group",
                )
                core.add_spacing(count=4, parent="workout_composition_group")
                core.add_button(
                    "Compose Workout##widget",
                    parent="workout_composition_group",
                    callback=self.compose_workout,
                )
                core.add_text(
                    "Fill all the inputs, please.",
                    color=[255, 0, 0],
                    parent="workout_composition_group",
                )
                simple.hide_item("Fill all the inputs, please.")
            elif self.tab_name == "Records":
                self._records = record_services.get_all_records_by_user(self._username)
                (
                    exercises,
                    times_exercises_done,
                ) = record_services.count_times_exercises_done_by_user(self._username)
                workouts_per_day = record_services.count_workouts_per_day_by_user(
                    self._username
                )
                core.add_table(
                    "record_table",
                    ["Exercise", "Sets", "Reps", "Date"],
                )
                for record_arr in self._records:
                    core.add_row("record_table", record_arr)
                pie_chart.generate_chart(data=times_exercises_done, labels=exercises)
                line_chart.generate_chart(
                    data=workouts_per_day,
                    labels=[i + 1 for i in range(len(workouts_per_day))],
                )

    def toggle(self):
        selected_rows = core.get_table_selections("workout_table")
        column = int(selected_rows[0][1])
        row = int(selected_rows[0][0])
        if column == 1:
            self._composed_workout[row]["Sets"] = (
                int(self._composed_workout[row]["Sets"]) + 1
            )
            core.set_table_item(
                "workout_table",
                row=row,
                column=column,
                value=str(self._composed_workout[row]["Sets"]),
            )
        elif column == 2:
            self._composed_workout[row]["Reps"] = (
                int(self._composed_workout[row]["Reps"]) + 1
            )
            core.set_table_item(
                "workout_table",
                row=row,
                column=column,
                value=str(self._composed_workout[row]["Reps"]),
            )
        elif column == 3:
            exercise_name = core.get_table_item("workout_table", column=0, row=row)
            example_link = workout_services.get_example_link_by_exercise(exercise_name)
            self.show_example(example_link)
        core.set_table_selection("workout_table", row=row, column=column, value=False)

    def save_workout(self):
        try:
            for workout in self._composed_workout:
                record_services.save_workout(
                    workout["Exercise"],
                    int(workout["Sets"]),
                    int(workout["Reps"]),
                    self._username,
                )
            core.add_text(
                "Results successfully saved",
                color=[0, 255, 0],
                parent="workout_execution_group",
            )
        except:
            core.add_text(
                "Error happened while saving the result",
                color=[255, 0, 0],
                parent="workout_execution_group",
            )
        self.cancel_workout()
        self._records = record_services.get_all_records_by_user(self._username)

    def cancel_workout(self):
        if core.does_item_exist("example_image"):
            core.delete_item("example_image")
        core.delete_item("buttons")
        core.delete_item("workout_table")
        simple.show_item("workout_composition_group")
        if core.get_value("Results successfully saved"):
            core.delete_item("Results successfully saved")
        if core.get_value("Error happened while saving the result"):
            core.delete_item("Results successfully saved")

    def show_example(self, link):
        if core.does_item_exist("example_image"):
            core.delete_item("example_image")
        response = requests.get(link)
        if response.status_code == 200:
            open(EXAMPLE_IMAGE_FILE_PATH, "wb").write(response.content)
            core.add_image(
                "example_image",
                EXAMPLE_IMAGE_FILE_PATH,
                parent="workout_execution_group",
            )

    def clear_table(self):
        for workout in self._composed_workout:
            workout["Sets"] = 0
            workout["Reps"] = 0
        core.clear_table("workout_table")
        for workout in self._composed_workout:
            core.add_row("workout_table", list(workout.values()))
