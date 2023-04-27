"""
Use ** operator to get power of a number.Use range() for loops.
Use list.append() to add values into a list.
"""

def print_square_list():
    squares = []
    for i in range(1,21):
        squares.append(i ** 2)
    print(squares)
    

def print_square_list2():
    print([x**2 for x in range(1,21)])

print_square_list()
print_square_list2()
    