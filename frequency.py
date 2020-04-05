import collections
class Freq:
    def __init__(self, list):
        self.list = list
    def fre(self):
        ctr = collections.Counter(self.list)
        print(ctr)
f1 = Freq([11,11,11,22,22,22,22,33,33,33,44,44,55,66])
f1.fre()