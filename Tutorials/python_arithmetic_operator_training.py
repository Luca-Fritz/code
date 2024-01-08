import random 
import math
import colorama as c

#running the loop to create new questions (random)
    #range 1x1 *30
def train_random():
    random_train = True
    while random_train == True:
        number_1 = random.randint(1, 30)
        number_2 = random.randint(1, 10)
        number_1 = number_1 * number_2
        solution = math.floor (number_1 / number_2)

        print (c.Fore.WHITE + "What is " + str(number_1) + " divided by " + str(number_2) + "?")
        user_input = input("Your answer: ").lower()
        if user_input == "exit":
            random_train = False
        elif user_input == str(solution):
            print(c.Fore.GREEN + "Thats right wanne try one more?\n")
        else:
            print(c.Fore.RED + "Thats wrong! It is " + str(solution) + "\n")


running = True
while running == True:
    #Get the training type the user wants to do
    user_choice = input("What do you wanna do? <random> / <number>: ").lower()
    print("<exit to exit>\n")

    if user_choice == "addition":
        rain_addition()
    elif user_choice == "subtraction":
        train_subtraction() 
        
    elif user_choice == "random":
        train_random()
    elif user_choice == "exit":
        running = False
    else:
        print("Please enter a vaild promt")
