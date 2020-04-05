from random import Shuffle


class Shuffle:
    def __init__(self, list):
        self.list = list

    def shu(self):
        Shuffle(self.list, None)


s1 = Shuffle(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])
s1.shu()
print(s1.list)
