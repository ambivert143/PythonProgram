h0=int(input('time khởi hành (giờ) : '))
m0=int(input("time khởi hành (phút):"))
h=int(input("time hiện tại (giờ): "))
m=int(input("time hiện tại (phút): "))
T=int(input("time đợi (phút) :  "))
t = (h0*60+m0)-(h*60+m)
t1 = (h0*60+m0)+(h*60+m)
while t > T:
    f = t-T
    t -= T  
e = t1 + f
print(f'{e//60}h{e%60}p')