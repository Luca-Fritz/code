#doubles every part in a string you enter 

user_input = input("Please enter your text: ")
final_list = []
final_String = ""

for part in user_input:
    final_list.append(part)
    final_list.append(part)

for part in final_list:
    final_String += " " + part

print (final_String)

