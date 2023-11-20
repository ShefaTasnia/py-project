import json

with open("data/meals.json") as file_1:
	meals = json.load(file_1)

with open("data/combos.json") as file_2:
	combos = json.load(file_2)

def show_task7():
    print("The meals from json file:")
    print(meals)
    print("\nThe combos from json file:")
    print(combos)

