from dearpygui import core, simple
from services.workout import workout_services
import requests
from PIL import Image
import random


class Tab:
    def __init__(self, tab_name, parent):
        self.tab_name = tab_name
        self.parent = parent
        self.composed_workout = None

    def cancel_workout(self):
        core.delete_item("workout_table")
        core.delete_item("buttons", children_only=True)
        core.delete_item("example_image")
        simple.show_item("workout_composition_group")

    def compose_workout(self):
        equipment_val = core.get_value("Equipment##widget")
        exercise_type_val = core.get_value("Exercise Type##widget")
        muscle_group_val = core.get_value("Muscle Group##widget")
        if not equipment_val or not exercise_type_val or not muscle_group_val:
            simple.show_item("Fill all the inputs, please.")
        else:
            simple.hide_item("workout_composition_group")
            self.composed_workout = workout_services.get_composed_workout(
                equipment_val, exercise_type_val, muscle_group_val
            )
            core.add_group("buttons")
            core.add_table(
                "workout_table",
                ["Exercise", "Sets", "Reps", "Example"],
                parent="workout_execution_group",
                callback=self.toggle,
            )
            for el in self.composed_workout:
                core.add_row("workout_table", list(el.values()))
            core.add_button(
                "Cancel##widget", callback=self.cancel_workout, parent="buttons"
            )
            core.add_button(
                "Clear##widget", callback=self.clear_table, parent="buttons"
            )
            core.add_button("Save##widget", parent="buttons", callback=save_workout)

    def generate(self):
        with simple.tab(name=self.tab_name, parent=self.parent):
            if self.tab_name == "Exercises":
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
            else:
                core.add_text(f"text 2")

    def save_workout(self):
        pass

    def toggle(self, sender, data):
        selected_rows = core.get_table_selections("workout_table")
        column = int(selected_rows[0][1])
        row = int(selected_rows[0][0])
        if column == 1:
            self.composed_workout[row]["Sets"] = (
                int(self.composed_workout[row]["Sets"]) + 1
            )
            core.set_table_item(
                "workout_table",
                row=row,
                column=column,
                value=str(self.composed_workout[row]["Sets"]),
            )
        elif column == 2:
            self.composed_workout[row]["Reps"] = (
                int(self.composed_workout[row]["Reps"]) + 1
            )
            core.set_table_item(
                "workout_table",
                row=row,
                column=column,
                value=str(self.composed_workout[row]["Reps"]),
            )
        elif column == 3:
            exercise_name = core.get_table_item("workout_table", column=0, row=row)
            example_link = workout_services.get_example_link_by_exercise(exercise_name)
            self.show_example(example_link)
        core.set_table_selection("workout_table", row=row, column=column, value=False)

    def show_example(self, link):
        try:
            response = requests.get(link)
            if response.status_code == 200:
                open("src/data/temp.gif", "wb").write(response.content)
                core.add_image(
                    "example_image",
                    "src/data/temp.gif",
                    parent="workout_execution_group",
                )
        except:
            simple.show_logger()
            core.log_debug("error")

    def clear_table(self):
        for el in self.composed_workout:
            el["Sets"] = 0
            el["Reps"] = 0
        core.clear_table("workout_table")
        for el in self.composed_workout:
            core.add_row("workout_table", list(el.values()))
