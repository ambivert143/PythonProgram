"""
num = [10,30,4,-6]
print(num.index(30))
"""
class Index:
    def __init__(self,list):
        self.list1 = list
        self.list2 = []
    def ind(self):
        self.list2 = list(self.list1)
        print(self.list2.index(30,0,3))
i1 = Index([10,30,4,-6])
i1.ind()