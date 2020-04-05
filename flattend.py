import itertools
class Flatt:
    def __init__(self,list):
        self.list1 = list
        self.list2 = []

    def flat(self):
        self.list2 = list(itertools.chain(*self.list1))

f1 = Flatt([[2,4,3],[1,5,6], [9], [7,9,0]])
f1.flat()
print(f1.list2)