from food_calories import calories

class MealTooBigError(Exception):
    
    def __init__(self, message="Meal exceeds 2000 cals"):
        self.message = message
        super().__init__(self.message)


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
            print("The item is not on the menu")
            return None
        
    if total_calories >2000:
        raise MealTooBigError
    
    return total_calories
    
def show_at4(given_order):
    print(calorie_counter(given_order))


