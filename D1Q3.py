#https://www.programiz.com/python-programming/dictionary-comprehension

def create_dictionary(n:int) -> dict:
    x2_dict = {}
    i = 1
    while i <= n:
        x2_dict.update({i:i * i})
        i += 1
    return x2_dict

def create_dict2(n:int):
    d = dict()
    for i in range(1,n+1):
        d[i] = i*i
    print(d)

def dictionary_comprehension(n:int):
    d = {x: x * x for x in range(1,n+1)}
    print(d)
        
    

n = int(input("Please give an integer: "))
print(create_dictionary(n))
create_dict2(n)
dictionary_comprehension(n)
