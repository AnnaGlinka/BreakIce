"""
Use dict[key]=value pattern to put entry into a dictionary.Use ** operator 
to get power of a number.Use range() for loops.
"""
def print_dic():
    squares = {}
    for i in range(1,21):
        squares[i] = i ** 2
    print(squares)

def print_dic2():
    print({x:x ** 2 for x in range(1,21)}) #Dictionary Comprehension

print_dic()
print_dic2()