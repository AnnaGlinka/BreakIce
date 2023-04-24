def devBy7andNot5(start:int, stop:int):
    print(*[x for x in range(start, stop+1) if x % 7 == 0 and x % 5 !=0],sep=",")
   

devBy7andNot5(2000, 3200)