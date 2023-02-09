class String:
    def __init__(self):
        self.Object = ""

    def getString(self):
        self.Object = input()

    def printString(self):
        print(self.Object.upper())

Object = String()
Object.getString()
Object.printString()