import random 
import math
import keyboard
abc = True

def run_func():
  print('Hi, welcome!')
  print('If you want to do this, press A or press B for doing that.')
  while abc:
    if keyboard.is_pressed('a'):
      train_with_number()
      abc = True

    elif keyboard.is_pressed('b'):
      train_random()
      abc = Trues

#if choice is to train with a specific number 
#range 1x1 *30
def train_with_number():
    num_train = True
    #Get the input and then running the loop to create new questions
    user_input = input("Enter the number you want to train with (1-10): ")
    while num_train == True:
        user_safe = user_input
        number_1 = random.randint(1, 10)
        number_1 = number_1 * int(user_safe)
        number_2 = int(user_safe)
        solution = math.floor (number_1 / number_2)

        print ("What is " + str(number_1) + " divided by " + str(number_2) + "?")
        user_answer = input("Your answer: ").lower()
        if user_answer == "exit":
            num_train = False
        elif user_answer == str(solution):
            print("Thats right wanne try one more?\n" + "<exit to exit>\n")
        else:
            print("Thats wrong! It is " + str(solution) + "\n" + "<exit to exit>\n")


#to train with random numbers
#range 1x1 *30
def train_random():
    random_train = True
    #running the loop to create new questions
    while random_train == True:
        number_1 = random.randint(1, 30)
        number_2 = random.randint(1, 10)
        number_1 = number_1 * number_2
        solution = math.floor (number_1 / number_2)

        print ("What is " + str(number_1) + " divided by " + str(number_2) + "?")
        user_input = input("Your answer: ").lower()
        if user_input == "exit":
            random_train = False
        elif user_input == str(solution):
            print("Thats right wanne try one more?\n" + "<exit to exit>\n")
        else:
            print("Thats wrong! It is " + str(solution) + "\n" + "<exit to exit>\n")

print('To start press S')
while abc:
  if keyboard.is_pressed('S'): 
    run_func()
  abc = True






