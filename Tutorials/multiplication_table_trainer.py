import random
ongoing = True 

while ongoing == True:

    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)

    user_input = input("what is " + str(number_1) + " times " + str(number_2) + "?" + "\n").lower()
    print("\n")
    solver = number_1 * number_2
    if user_input == "stop":
        ongoing = False
    
    elif user_input == str(solver):
        print("Congrats you got the task right! \n stop to end the task")
        print("\n")
    
    else:
        print(str(number_1) + " times " + str(number_2) + " is " + str(solver) + " and not " + user_input)
        print("\n")