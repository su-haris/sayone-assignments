class myCircle:
    def calcRadius(self):
        r = int(input('Enter radius'))
        area = 3.14*r*r
        print('Area is', area)

    def __init__(self):
        self.calcRadius()


o = myCircle()