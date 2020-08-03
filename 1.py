"""
for i in range(100,1000):
    S =(i//100) + (i%100//10) + (i%100)
    if S == 9:
        print(i)
"""



lst1=[0,1,2,3,4,5,6,7,8,9]
lst2=[0,1,2,3,4,5,6,7,8,9]
lst3=[0,1,2,3,4,5,6,7,8,9]
S=0
for x in range(len(lst1)):
    for y in range(len(lst2)):
        for z in range(len(lst3)):
            if (x+y+z)==9:
             S=(int(f"{x}{y}{z}"))
             if 100<S<1000:
              print(S)