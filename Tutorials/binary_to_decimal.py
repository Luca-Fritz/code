import numpy 

position = 0
power = 1
result = []
user_input = input("Input your binary number: ")
str_user_input = int(user_input)
ar_user_input = [int(x) for x in str(str_user_input)]
ar_user_input = ar_user_input[::-1]

print (str_user_input)
print (ar_user_input)

#while position != len(ar_user_input):
for x in ar_user_input:
    if ar_user_input[position] == 1:
        result.append(pow(position, power))
        position =+ 1
        power =+ 1
        print("ist 1")

    elif ar_user_input[position] == 0:
        result.append(0)
        position =+ 1
        power =+ 1
        print("ist 2")
    else:
        print("Hier ist was falsch gelaufen")

print(result)