#https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%202.md

class ExampleClass:
    def __init__(self):
        self.console_input = ""

    def getString(self):
        self.console_input = input("Please add some input: ")

    def printString(self):
        print(self.console_input.upper())

ec = ExampleClass()
ec.getString()
ec.printString()