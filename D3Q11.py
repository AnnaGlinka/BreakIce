#0100,0011,1010,1001,1010
def divisible_by_5(num: str) -> bool:
    to_pow = 3
    sum = 0
    for ch in num:
        sum += int(ch) * pow(2, to_pow)
        to_pow -= 1
    return sum % 5 == 0
  

binary_numbers = input("provide the list of binary numbers to check: ").split(",")
result = []
for num in binary_numbers:
    if divisible_by_5(num):
        result.append(num)

print(",".join(result))   



