"""
D 300
D 300
W 200
D 100
"""

trans_list = []

while True:
    transaction = input()
    if transaction:
        trans_list.append(transaction)
    else:
        break

net_ammount = (sum(int(tran[2:]) for tran in trans_list if tran[0]=='D') - 
                sum(int(tran[2:]) for tran in trans_list if tran[0]=='W'))
print(net_ammount)
