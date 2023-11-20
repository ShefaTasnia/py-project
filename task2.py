from food_calories import combos
from task1 import calorie_counter

def combo_calories_counter(ordered_combo):
	if ordered_combo in combos:
		combo_meal = combos[ordered_combo]
		#calling the already defined function, reducing redundancy 
		total_cal = calorie_counter(combo_meal)
		return total_cal
	else:
		print("Item not in combo meals")
    	
def show_task2(given_combo):
	print("Total calorie in given combo = " +  str(combo_calories_counter(given_combo)))
