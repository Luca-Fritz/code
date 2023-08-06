import random 
import math

#Lists of 1x1
running = True
while running == True:
    num_train = True
    random_train = False

    user_choice = "number"

    #if choice is to train with a specific number 
    

    #if choice is to train with a specific number 
    if user_choice == "number":
        user_input = input("Enter the number you want to train with (1-10): ")

        while num_train == True:
            user_safe = user_input
            number_1 = random.randint(1, 30)
            number_1 = number_1 * int(user_safe)
            number_2 = int(user_safe)
            solution = math.floor (number_1 / number_2)

            print ("What is " + str(number_1) + " divided by " + str(number_2) + "?")
            user_answer = input("Your answer: ").lower()
            if user_answer == "exit":
                num_train = False
            elif user_answer == str(solution):
                print("Thats right wanne try one more? (Exit to exit) \n")
            else:
                print("Thats wrong! It is " + str(solution) + "\n")
    
    #to train with random numbers from 2-100 / 2-9
    elif user_choice == "random":
        while random_train == True:
                number_1 = random.randint(2, 100)
                number_2 = random.randint(2, 9)
                solution = math.floor (number_1 / number_2)

                print ("What is " + str(number_1) + " divided by " + str(number_2) + "?")
                user_input = input("Your answer: ").lower()
                if user_input == "exit":
                    random_train = False
                elif user_input == str(solution):
                    print("Thats right wanne try one more? (Exit to exit) \n")
                else:
                    print("Thats wrong! It is " + str(solution) + "\n")

    elif user_choice == "exit":
        running = False
