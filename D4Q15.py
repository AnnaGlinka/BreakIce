a = "9"
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print(n1,n2,n3,n4)
print(n1+n2+n3+n4)

#-------------------------------------
sum = 0
for i in range(1,5):
    sum += int(i*a)

print(sum)

#----------------------------------------

