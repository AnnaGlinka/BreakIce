"""
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85

name > age > score
https://docs.python.org/3/howto/sorting.html
itemgetter - multiple levels of sorting
"""
from operator import itemgetter

list_of_records = []
while True:
    inp = input()
    if not inp:
        break
    list_of_records.append(tuple(inp.split(",")))

print(sorted(list_of_records, key=itemgetter(0,1,2)))