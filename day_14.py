class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=0

    def computeDifference(self):
        for i in self.__elements:
            for j in self.__elements: 
                resta= abs(i-j)
                if resta>self.maximumDifference:
                    self.maximumDifference=resta       
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
