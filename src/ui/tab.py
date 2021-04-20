from dearpygui import core, simple
from services.workout import (
    get_criterias_by_name,
    get_composed_workout,
    get_example_link_by_exercise,
)
import requests


class Tab:
    def __init__(self, tab_name, parent):
        self.tab_name = tab_name
        self.parent = parent
        self.composed_workout = None

    def compose_workout(self):
        equipment_val = core.get_value("Equipment##widget")
        exercise_type_val = core.get_value("Exercise Type##widget")
        muscle_group_val = core.get_value("Muscle Group##widget")
        if not equipment_val or not exercise_type_val or not muscle_group_val:
            simple.show_item("Fill all the inputs, please.")
        else:
            self.composed_workout = get_composed_workout(
                equipment_val, exercise_type_val, muscle_group_val
            )
            simple.hide_item("workout_composition_group")
            core.add_table(
                "Workout", ["Exercise", "Sets", "Reps", "Example"], callback=self.toggle
            )
            for el in self.composed_workout:
                core.add_row("Workout", list(el.values()))
            core.add_button("Cancel##widget")
            core.add_button("Save##widget")

    def generate(self):
        with simple.tab(name=self.tab_name, parent=self.parent):
            if self.tab_name == "Exercises":
                core.add_spacing(count=10)
                core.add_group(name="workout_execution_group")
                core.add_group(name="workout_composition_group")
                core.add_combo(
                    "Equipment##widget",
                    items=get_criterias_by_name("Equipment"),
                    parent="workout_composition_group",
                )
                core.add_spacing(count=4, parent="workout_composition_group")
                core.add_combo(
                    "Exercise Type##widget",
                    items=get_criterias_by_name("Exercise Type"),
                    parent="workout_composition_group",
                )
                core.add_spacing(count=4, parent="workout_composition_group")
                core.add_combo(
                    "Muscle Group##widget",
                    items=get_criterias_by_name("Major Muscle"),
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

    def toggle(self, sender, data):
        selected_rows = core.get_table_selections("Workout")
        column = selected_rows[0][1]
        row = selected_rows[0][0]
        if int(column) == 0:
            pass
        elif int(column) == 3:
            exercise_name = core.get_table_item("Workout", column=0, row=row)
            example_link = get_example_link_by_exercise(exercise_name)
            self.show_example(example_link)

        core.set_table_selection("Workout", row=row, column=column, value=False)

    def show_example(self, link):
        try:
            response = requests.get(link)
            if response.status_code == 200:
                open("src/data/temp.gif", "wb").write(response.content)
                core.add_image("canvas", "src/data/temp.gif")
        except:
            simple.show_logger()
            core.log_debug("error")
