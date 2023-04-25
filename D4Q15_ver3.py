from functools import reduce

a = "9"

def my_add(x, y):
    return int(x) + int(y)

print(reduce(my_add, [a*i for i in range(1,5)]))