class MyClass:
    a, b = 0, 0 #class parameter

    def __init__(self, a=None, b=None):
        self.a = a #self.a - instance parameter
        self.b = b


A = MyClass()
print(A.a, A.b)
A.a = 10
A.b = 20
print(A.a, A.b)

x = MyClass(1, 2)
y = MyClass(4, 5)

print(x.a, y.b)


