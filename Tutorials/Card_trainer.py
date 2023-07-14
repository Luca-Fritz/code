import random
ongoing = True 

while ongoing == True:

    number_1 = random.randint(7, 11)
    number_2 = random.randint(7, 11)
    number_3 = random.randint(7, 11)
    result = number_1 + number_2 + number_3

    print(number_1)
    print(number_2)
    print(number_3)
    print("\n")

    user_input = input("add the numbers: ").lower()

    if user_input == "stop":
        ongoing = False 
    elif user_input == str(result):
        print("The Result is right")
        print("--------------------------------------------")
        print("\n")
    else:
        print("thats wrong! Type Stop to end")
        print("--------------------------------------------")
        print("\n")
