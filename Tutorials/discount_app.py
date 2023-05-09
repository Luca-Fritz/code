#applying a dicount to a price 

full_price = input("Enter the full price: ")
full_price = int(full_price)
discount = input("Enter the discount(without %): ")
discount = int(discount) / 100
discount = discount * full_price

discounted_price = full_price - discount
print("The discounted price is " + str(discounted_price))
