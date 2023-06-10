import random

test = ["1", "2", "3", "4"]
test_int = test[random.randint(0, 3)]
abc = "What is " + " + ".join(test)
print (abc)