#error in test should be 0 7

class Generator:
    def generate_number(self, end:int):
        for x in range(end + 1):
            if x % 7 == 0: 
                yield x

g = Generator()

result = g.generate_number(int(input("Please insert a positive number: ")))
for x in result:
    print(x)