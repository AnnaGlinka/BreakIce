#1000 and 3000 

def is_even(char:str) -> bool:
    return int(char) % 2 == 0

result = [str(x) for x in range(1000, 3001) if all(map(is_even ,str(x)))]
print(",".join(result))