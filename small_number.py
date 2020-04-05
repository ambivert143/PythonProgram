class Small_Number:
    def __init__(self, list):
        self.list = list
    def sma(self):
        for x in range(len(self.list)):
            for y in range(len(self.list)):
                if self.list[x] > self.list[y]:
                    self.list[x], self.list[y] = self.list[y], self.list[x]
        print(self.list[-2])
s1 = Small_Number([1,2,-8,-2,0,-2])
s1.sma()