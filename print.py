""" color = [x for (i,x) in enumerate(color) if i not in (0,4,5)] ???
print(color)
"""
class Print:
    def __init__(self, list):
        self.list = list
        self.list1 = []
    def pri(self):
        self.list1 = [x for (i,x) in enumerate(self.list) if i not in (0,4,5)]
p1= Print(['red', 'blue','black','pink'])
p1.pri()
print(p1.list1)