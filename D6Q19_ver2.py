"""
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85

name > age > score
https://docs.python.org/3/howto/sorting.html
"""

list_of_records = []
while True:
    inp = input()
    if not inp:
        break
    list_of_records.append(tuple(inp.split(",")))

list_of_records.sort(key= lambda x:(x[0], int(x[1]), int(x[2])))
print(list_of_records)