user_input = input("Input the text in which you want to compare the x's to the o's: ").lower()
equal = True
o_count = 0
x_count = 0

for letter in user_input:
    if letter == "x":
        x_count += 1

    if letter == "o":
        o_count += 1

print ("\n" + "o-Count: " + str(o_count) + " / x-count: " + str(x_count))
if x_count == o_count:
    print("the x's equal the o's ")
    equal = True

else:
    print("the x's dont equal the o's ")
    equal = False
