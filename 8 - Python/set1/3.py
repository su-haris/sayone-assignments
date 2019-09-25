class Test:
    def getString(self):
        self.ins = input('Enter a string')

    def printString(self):
        print('Entered string is', self.ins)

    def __init__(self):
        self.ins = None
        self.getString()
        self.printString()


m = Test()
