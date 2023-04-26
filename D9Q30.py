def print_longer(a:str, b:str):
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        print(a)
    elif len_b > len_a:
        print(b)
    else:
        print(a,b)

print_longer("Ewa","Ala")
print_longer("Ewa","Alicja")

print_longer2 = (lambda a, b: print(a) if len(a) > len(b) 
                 else (print(b) if len(b) > len(a) else print(a, b)))

func = lambda a,b: print(max((a,b),key=len)) if len(a)!=len(b) else print(a+'\n'+b)

print_longer2("mama", "baba")
print_longer2("mama", "babcia")