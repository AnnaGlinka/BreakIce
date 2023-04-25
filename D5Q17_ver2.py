"""
D 300
D 300
W 200
D 100
"""

net_amount = 0

while True:
    trasaction = input().split(" ")
    if trasaction == ['']:
        break

    if trasaction[0] == 'D':
        net_amount += int(trasaction[1])
    else:
        net_amount -= int(trasaction[1])
    

print(net_amount)