#This trainer should help you to train binary network addresse calculation
#
#Imports
import random
#
#Code

user_input = input("How many integers at once? \n !!for example 2 = 128 + 8 or 3 = 64 + 32 + 4!! \n Your Input: ")
print ("\n")

user_int = int(user_input)

#The list of binary data and the random selection of one of them
bin_list = ["128", "64", "32", "16", "8", "4", "2", "1"]


#Creating the task to the users wish
task_list = []

for x in bin_list:
    if len(task_list) == user_int:
        break
    else:
        bin_int = bin_list[random.randint(0, 7)]
        task_list.append(bin_int)
        
task = "What is " + " + ".join(task_list)
print (int(task_list))
print(task)
