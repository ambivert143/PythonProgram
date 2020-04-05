class Comm:
    def __init__(self, list1,list2):
        self.list1 = list1
        self.list2 = list2
    def com(self):
        for x in self.list1:
            for y in self.list2:
                if x==y:
                    return 'True'
c1 = Comm([3,4,33,44,55,66],[2,5,25,22,55])
c1.com()
print(c1.com())