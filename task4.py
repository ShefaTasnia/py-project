from food_calories_complex import combos_complex, meals_complex

def order_combo(combo_id):
    try:
        combo = next(item for item in combos_complex if item["id"] == combo_id)
        ordered_meals = [next(meal for meal in meals_complex if meal["id"] == meal_id) for meal_id in combo["meals"]]
        print("Given Order :", combo["name"])
        print("Meals in order :", [meal["name"] for meal in ordered_meals])
        print("Price of order: ", combo["price"], "\n")
    except StopIteration:
        print("The item is not on the menu")

def order_meal(meal_name):
    try: 
        ml = [next(meal for meal in meals_complex if meal["name"] == meal_name)]
        ml_dict = ml[0]
        print("Given Order :", ml_dict["name"])
        print("Price of meal: ", ml_dict["price"])
    except StopIteration:
        print("Item not in menu")

def show_task4(given_order):
    #ordering a combo
    order_combo(given_order)

