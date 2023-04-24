from math import sqrt

def calculate(values:list):
    for num in values:
        #Q = Square root of [(2 _ C _ D)/H]
        print(round(sqrt((2*50*num)/30)),end=",")
    
L = [int(x) for x in (input("Please add the list of numbers for calculation: ").split(","))]
print(L)
calculate(L)
