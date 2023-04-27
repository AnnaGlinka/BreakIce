#Define a class named American which has a static method called printNationality.
#https://realpython.com/instance-class-and-static-methods-demystified/

class American:
    def __init__(self, nationality="American"):
        self.nationality = nationality

    @staticmethod
    def printNationality():
        print("American")


anAmerican = American("Afro-american")
print(anAmerican.nationality)
anAmerican.printNationality()
American.printNationality()
print(American.nationality)