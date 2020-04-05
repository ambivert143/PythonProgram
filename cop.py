class Cop:
    def __init__(self,list):
        self.list = list
        self.list1 = []
    def clone(self):
        self.list1 = list(self.list)
c1 = Cop([1,2,3,444,555])
c1.clone()
print(c1.list1)