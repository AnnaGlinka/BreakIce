def even(my_tuple:tuple):
    for i in my_tuple:
        if i % 2 == 0:
            print(i,end=" ")

even((1,2,3,4,5,6,7,8,9,10))

my_tpl = (1,2,3,4,5,6,7,8,9,10)
even = tuple(filter(lambda x : x%2 == 0, my_tpl))  
                                             
print(even)