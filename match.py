"""
def match(words)
  ctr =0
  for word in words:
    if len(word)>1 and word[0] == word[-1]:
       ctr += 1
  return ctr
print(match(['abc','zxc','aba','1221']))
"""


class Match_word:
    def __init__(self, list):
        self.list = list
        self.ctr = 0

    def mat(self):
        for word in self.list:
            if len(word) > 1 and word[0] == word[-1]:
                self.ctr += 1


M1 = Match_word(['aba', 'xbo', 'cbe'])
M1.mat()
print(M1.ctr)
