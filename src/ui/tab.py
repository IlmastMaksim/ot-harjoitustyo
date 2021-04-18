from dearpygui.core import *
from dearpygui.simple import *
from ui.table import Table
from services.workout import get_criterias_by_name, get_composed_workout
import requests


class Tab:
    def __init__(self, tab_name, parent):
        self.tab_name = tab_name
        self.parent = parent
        self.composed_workout = None

    def show_example(self):
            try:
                response = requests.get("https://dl.airtable.com/KNCrgmAZTKyppbcj7oTC_a562d6f5-888c-4b4a-a274-f969c3a8557d.gif")
                if response.status_code == 200:
                    open('src/data/temp.gif', 'wb').write(response.content)
                    add_image("canvas", "src/data/temp.gif")
                    # download image, turn file into a texture, draw on a canvas, delete image when image is closed)
            except:
                show_logger()
                log_debug("error")  

    def compose_workout(self):
        equipment_val = get_value("Equipment##widget")
        exercise_type_val = get_value("Exercise Type##widget")
        muscle_group_val = get_value("Muscle Group##widget")
        if not equipment_val or not exercise_type_val or not muscle_group_val:
            show_item('Fill all the inputs, please.')
        else:
            self.composed_workout = get_composed_workout(equipment_val, exercise_type_val, muscle_group_val)
            hide_item("workout_composition_group")
            table_1 = Table("Workout")
            table_1.add_header(["Exercise", "Sets", "Reps", "Example", "Completed"])
            for el in self.composed_workout:
                table_1.add_row(el.values())
            add_button("Cancel##widget")
            add_button("Save##widget") 
            

    def generate(self):
        with tab(name=self.tab_name, parent=self.parent):
            if self.tab_name == "Exercises":
                add_spacing(count=10)
                add_group(name="workout_execution_group")
                add_group(name="workout_composition_group")
                add_combo("Equipment##widget", items=get_criterias_by_name("Equipment"), parent="workout_composition_group")
                add_spacing(count=4, parent="workout_composition_group")
                add_combo("Exercise Type##widget", items=get_criterias_by_name("Exercise Type"), parent="workout_composition_group")
                add_spacing(count=4, parent="workout_composition_group")
                add_combo("Muscle Group##widget", items=get_criterias_by_name("Major Muscle"), parent="workout_composition_group")
                add_spacing(count=4, parent="workout_composition_group")
                add_button("Compose Workout##widget", parent="workout_composition_group", callback=self.compose_workout)
                add_text('Fill all the inputs, please.', color=[255, 0, 0], parent='workout_composition_group')
                hide_item('Fill all the inputs, please.')
            else:
                add_text(f'text 2')