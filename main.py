from food_calories import calories, combos
from task1 import show_task1
from task2 import show_task2
from task3 import show_task3
from task4 import show_task4
from task5 import show_task5
from task7 import show_task7
from task8 import show_task8
from advance_task3 import show_at3
from advance_task4 import show_at4

print("-------------CALORIE COUNTER PROJECT-----------")
print("Option: \n 1. Create a basic calorie counter \n 2. Handle Combo \n 3. Handle Error \n 4. Use More Complex Data \n 5. Create a Price counter \n 6. Store Json \n 7. Use OOP to handle orders")
print(" 8. Use recursive function to count Calorie (Advance Task 3) \n 9. Create a custom exception (Advance task 4) \nPRESS X TO EXIT")

while(True):
    choice = input("Enter choice number (PRESS X TO EXIT) : ")

    if choice == str(1):

        print("Chosen option 1 (Create a basic calorie counter)\n")
        meal_list_t1 = ["Hamburger", "Lemonade", "Salad"]
        print ("Given order = " + str(meal_list_t1))
        show_task1(meal_list_t1)
        
    elif choice == str(2):

        print("Chosen option 2 (Handle Combo) \n")
        given_combo = "Cheesy Combo"
        print ("Given order = " + given_combo)
        show_task2(given_combo)

    elif choice == str(3):

        print("Chosen option 3 (Handle Error) \n")
        meal_list_t3 = ['Biriani']
        print("Given meal list = " + str(meal_list_t3))
        show_task3(meal_list_t3)

    elif choice == str(4):

        print("Chosen option 4 (Use More Complex Data)\n")
        given_order_t4 = "combo-1"
        print("Given order = " + given_order_t4)
        show_task4(given_order_t4)

    elif choice == str(5):

        print("Chosen option 5 (Create a Price counter) \n")
        given_order_t5 = "cheesy combo"
        print("Given order = " + given_order_t5)
        show_task5(given_order_t5)

    elif choice == str(6):

        print("Chosen option 6 (Show store Json data) \n")
        show_task7()

    elif choice == str(7):

        print("Chosen option 7 (Use OOP to handle orders)\n")
        given_order_t7 = ["meal-2", "meal-5", "meal-8"]
        print("Given order = " + str(given_order_t7))
        show_task8(given_order_t7)

    elif choice == str(8):

        print("Chosen option 8 : Use recursive function to count Calorie (Advance Task 3)\n")
        given_order_t8 = ["combo-1", "combo-3"]
        print("Given order = " + str(given_order_t8))
        show_at3(given_order_t8)

    elif choice == str(9):

        print("Chosen option 9: Create a custom exception (Advance task 4)\n")
        given_order_t9 = ['Sweet Potatoes', 'Iced Tea', 'Lemonade', 'Hamburger', 'Hamburger', 'Hamburger']
        print("Given order = " + str(given_order_t9))
        show_at4(given_order_t9)
    
    elif choice == 'x' or 'X':
        break

