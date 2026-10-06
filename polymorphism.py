# 1
class Animal:
    def make_sound(self):
        print("animal sound")
class Dog(Animal):
    def start(self):
        print("dog sounds" " boww")
class Cat(Animal):
    def start(self):
        print("cat sounds" " meoww")
class Cow(Animal):
    def start(self):
        print("cow sounds" " ambaa")
# l=[Dog(),Cat(),Cow()]
# for i in l:
#     i.start()


# 2
def operate(device):
    device.start()
class Car:
    def start(self):
        print("car")
class Computer:
    def start(self):
        print("computer")
class WashingMachine:
    def start(self):
        print("washing machine")
l=[Car(),Computer(),WashingMachine()]
# for i in l:
#     # operate(i)
#     i.start()


# 3
class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return vector(self.x+other.x,self.y+other.y)
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

# v1=vector(2,3)
# v2=vector(4,5)
# v3=v1+v2
# print(v3.x,v3.y)
# print(v3==v2)
# v4=vector(6,8)
# print(v3==v4)


# 4
class Transport:
    def move(self):
        print("moving",end=" ")
class Bus(Transport):
    def move(self):
        # print("bus")
        super().move()
        print("bus")
class Bike(Transport):
    def move(self):
        super().move()
        print("bike")
# b=Bus()
# b.move()
# b1=Bike()
# b1.move()


# 6
class Payment:
    def process(self,amount):
        print(f"{amount} paid",end=" ")
class creditCardPayment(Payment):
    def process(self,amount,card_type):
        super().process(amount)
        print(f"using {card_type} to pay")
        # super().process(amount)

# c=creditCardPayment()
# # c.process(1000)   it gives an error
# c.process(10000,"sbi")


# 7
class sorter:
    def change(self,strategy):
        strategy.logic()
class BS:
    def logic(self):
        print("binary sort")
class MS:
    def logic(self):
        print("merge sort")
class QS:
    def logic(self):
        print("quick sort")

# l=[BS(),QS(),MS()]
# for i in l:
#     i.logic()
#
#     # (or)
#
# s=sorter()
# l=[BS(),QS(),MS()]
# for i in l:
#     s.change(i)


# 8
class Account:
    def withdrawn(self,amount):
        print(f"{amount} withdrawn")
class SavingsAccount(Account):
    def withdrawn(self,amount):
        print("savings account",end=" ")
        super().withdrawn(amount)
class PremiumSavingsAccount(Account):
    def withdrawn(self,amount):
        print("premium account",end=" ")
        super().withdrawn(amount)

# l=[Account(),SavingsAccount(),PremiumSavingsAccount()]
# for i in l:
#     i.withdrawn(1000)
#
# #     (or)
#
# def withdrawn(obj):
#     obj.withdrawn(1000)
# withdrawn(Account())
# withdrawn(SavingsAccount())
# withdrawn(PremiumSavingsAccount())


# 9
def draw(shape):
    shape.draw()
class Circle:
    def draw(self):
        print("drawing a circle")
class Square:
    def draw(self):
        print("drawing a square")
class Rectangle:
    def draw(self):
        print("drawing a rectangle")
class Car:
    def draw(self):
        print("drawing a car")

# l=[Circle(),Square(),Rectangle(),Car()]
# for i in l:
#     i.draw()
#
# #     (or)
#
# draw(Circle())
# draw(Square())
# draw(Rectangle())
# draw(Car())


# 10
class Payment:
    def pay(self,amount):
        print(f"{amount} is paid")
class upi(Payment):
    def pay(self,amount):
        print("upi")
        super().pay(amount)
class card(Payment):
    def pay(self,amount):
        print("card")
        super().pay(amount)
class cash(Payment):
    def pay(self,amount):
        print("cash")
        super().pay(amount)
# def pay(obj):
#     obj.pay(500)
def ipay(obj):
    if isinstance(obj,upi):
        obj.pay(100)
    elif isinstance(obj,card):
        obj.pay(200)
    else:
        obj.pay(300)
l=[upi(),card(),cash()]
for i in l:
    i.pay(500)
    ipay(i)