#displays a list of numbers normal, descending or ascending  
import sort_list

numbers = input ("Please enter the numbers you want to sort seperated by a space: ")
print("\n")
list = numbers.split()
for i in range(len(list)):
    list[i] = int(list[i])


type = input("Plese choose between asc, desc or none: ") 

if type == "asc":
    list.sort()
    print(list)

elif type == "desc":
    list.sort(reverse=True)
    print(list)

elif type == "none":
        print(list)
else:
        print("The type you entered does not exitst!")



