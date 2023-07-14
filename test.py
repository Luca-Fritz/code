import random

test = ["11", "233", "333", "433"]
test_int = test[random.randint(0, 3)]
abc = "What is " + " + ".join(test)
print (abc)