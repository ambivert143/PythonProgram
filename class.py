# ex1:tạo lớp và đối tượng
class Parrot:
    species = "bird"  # thuộc tính lớp

    def __init__(self, name, age):  # thuộc tính thể hiện
        self.name = name
        self.age = age


# khởi tạo lớp Parrot
blu = Parrot("blu", 10)
woo = Parrot("woo", 15)
# truy cập các thuộc tính lớp
print("blu is a {}".format(blu.__class__.species))
print("woo is also a {}".format(woo.__class__.species))
# truy cập thuộc tính thể hiện
print("{} is {} year old".format(blu.name, blu.age))
print("{} is {} year old".format(woo.name, woo.age))


# ex2:phương thức
class Parrot:
    # thuộc tính thể hiện
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # thuộc tính phương thức
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


# khởi tạo lớp đối tượng
blu = Parrot("blu", 10)
# gọi phương thức cá thể
print(blu.sing("happy"))
print(blu.dance())


# ex3:kế thừa
# lớp cha
class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("swim faster")


# lớp con
class Penguin(Bird):
    def __init__(self):
        # gọi hàm supper()
        super().__init__()
        print("Renguin is ready")

    def whoisThis(self):
        print("Renguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


# ex4:đóng gói dữ liệu
class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()
# thay đổi giá trị
c.__maxprice = 1000
c.sell()
# sử dụng hàm set
c.setMaxPrice()
c.sell()


# ex5:đa hình
class Parrot:
    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin:
    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")


# giao thức
def flying_test(bird):
    bird.fly()


# khởi tạo đối tượng
blu = Parrot()
peggy = Penguin()
# vượt qua đối tượng
flying_test(blu)
flying_test(peggy)
