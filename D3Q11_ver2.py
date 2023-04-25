#0100,0011,1010,1001,1010
def divisible_by_5(num: str) -> bool:
    return int(num,2) % 5 == 0      # int(num,b) takes x as string and b as base from which
    

binary_numbers = input("provide the list of binary numbers to check: ").split(",")
result = filter(divisible_by_5, binary_numbers)

print(",".join(result))





