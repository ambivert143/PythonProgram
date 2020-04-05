class Append:
    def __init__(self, list1,list2):
        self.list1 = list1
        self.list2 = list2
    def app(self):
        x = self.list1 +self.list2
        print(x)
a1= Append([1,2,3,4],['red', 'blue','black'])
a1.app()