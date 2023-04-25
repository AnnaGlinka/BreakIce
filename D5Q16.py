#1,2,3,4,5,6,7,8,9

numbers = input("input a list of numbers separated by comma: ").split(",")

square_odd = [str(int(x)**2) for x in numbers if int(x) % 2]
print(",".join(square_odd))