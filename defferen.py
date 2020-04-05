class Deff:
    def __init__(self, list1,list2):
        self.list1 = list1
        self.list2 = list2
        self.list_def = []
    def deff(self):
        self.list_def = (list(set(self.list1)-set(self.list2)))
d1 = Deff([1,2,3,4,5],[3,4,5])
d1.deff()
print(d1.list_def)
