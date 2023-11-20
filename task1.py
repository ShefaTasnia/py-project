from food_calories import calories

def calorie_counter(meals):
    #initializing total calory to 0
    total_calories = 0

    # meals is now a list with food names
    # if the food is in the dictionary, accummulate
    # else print an error message 
    for meal in meals:
        try: 
            # meal in calories:
            total_calories += calories[meal]
        except:
            print("The item " + meal + " is not on the menu")
            return None
    return total_calories

def show_task1(meal_list):
    total_calories = calorie_counter(meal_list)
    print("Total calorie for given order = " + str(total_calories))
