#only diplays the numbers from an input

user_input = input("Please enter the text you want the integers out of: ").lower()
number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

final_list = []

for part in user_input:
    if part in number_list:
        final_list.append(part)

print (final_list)        
