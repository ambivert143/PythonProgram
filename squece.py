class Square:
    def __init__(self, list):
        self.list = list
        self.list1 = []
    def squa(self):
        for x in self.list:
            self.list1.append(x ** 2)


s1 = Square(list(range(31)))
s1.squa()
print(s1.list1[4:])