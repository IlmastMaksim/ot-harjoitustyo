import json

def get_exercises_with_dumbbells():
    with open("./src/data/dataset.json", "r") as read_file:
        data = json.load(read_file)
        exercises_with_dumbbells = []
        for el in data:
            if "Dumbbells" in el["Equipment"]:
                exercises_with_dumbbells.append(el)
        return exercises_with_dumbbells