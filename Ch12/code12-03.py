from random import *

for x in range(5) :
    numbers = list(range(1, 50))
    numbers = sample(numbers, 6)
    print("{0} : {1}".format(x+1, numbers))
