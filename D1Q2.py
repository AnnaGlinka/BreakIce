#https://realpython.com/python-reduce-function/
from functools import reduce

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
def factorial2(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def multiply(x,y):
    return x*y
def factoral_with_reduce(n):
    return reduce(multiply, range(1,n+1))
    
        


n = input("Please privide a number (belongs to N): ")
n = int(n)
print(factorial(n))
print(factorial2(n))
print(factoral_with_reduce(n))

