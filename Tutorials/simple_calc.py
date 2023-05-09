integer_1 = input("Enter the first number: ")
#a simple calculator which can solve +, -, /, * requests 

integer_1 = int(integer_1)

operator = input("Enter your operator +, -, /, * : ")

integer_2 = input("Enter second number: ")
integer_2 = int(integer_2)

solution = 0

if operator == "+": 
    solution = integer_1 + integer_2
elif operator == "-":
    solution = integer_1 - integer_2
elif operator == "/":
    solution = integer_1 / integer_2
else:
    solution = integer_1 * integer_2

print("The solution is " + str(solution))
