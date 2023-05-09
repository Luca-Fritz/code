#only shows the last four digits of the number you enter

card_number = input("Enter credit card number: ")
censor = len(card_number) - 4
card_number = card_number[censor:]
print(card_number)