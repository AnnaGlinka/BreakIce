def print_square_val():
    d={x:x**2 for x in range(1,21)}
    for k,v in d.items():
        print(k, end=",")
    print("")

def print_square_val2():
    d={x:x**2 for x in range(1,21)}
    print(d.keys())


print_square_val()
print_square_val2()