from food_calories_complex import meals_complex, combos_complex

def calorie_counter_recursive(items, meals_list, combos_list):
    total_calories = 0

    for item_id in items:
        item = next((meal for meal in meals_list if meal["id"] == item_id), None)

        if item:
            total_calories += item["calories"]

        else:
            combo = next((combo for combo in combos_list if combo["id"] == item_id), None)

            if combo:
                total_calories += calorie_counter_recursive(combo["meals"], meals_list, combos_list)

    return total_calories

def show_at3(given_order):
     
    total_calories = calorie_counter_recursive(given_order, meals_complex, combos_complex)
    print(f"Total calories for the order: {total_calories}")
