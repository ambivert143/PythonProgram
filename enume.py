class Enum:
    def __init__(self,list):
        self.list = list
    def enume(self):
        for index, val in enumerate(self.list,start=1):
            print(index,val)
e1 = Enum([5,15,45,4,53])
e1.enume()