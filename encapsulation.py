class A:
    def __init__(self,x,y):
        self._x=x
        self.__y=y
# a=A(1,2)
# print(a._x)
# # print(a.__y)   // it gives an error we should not write like this
# print(a._A__y)


class A:
    def __init__(self,x,y):
        self._x=x
        self.__y=y
    def get_x(self):
        return self._x
    def get_y(self):
        return self.__y
    def set_x(self,x):
        self._x=x
    def set_y(self,y):
        self.__y=y
# a1=A(5,6)
# print(a1.get_x())
# print(a1.get_y())
# a1.set_x=1
# print(a1.set_x)
# a1.set_y=9
# print(a1.set_y)


class A:
    def __init__(self,name,age):
        self._name=name
        self.__age=age
    def get_x(self):
        return self._name
    def get_y(self):
        return self.__age
    def set_x(self,n):
        self._name=n
    def set_y(self,a):
        self.__age=a
# a=A("m",21)
# print(a.get_x())
# print(a.get_y())
# a.set_x("n")
# a.set_y(25)
# print(a.get_x())
# print(a.get_y())


class A:
    def __init__(self,name,age):
        self._name=name
        self.__age=age
    @property
    def a(self):
        return self._name
    @property
    def b(self):
        return self.__age
# n=A("a",22)
# print(n.a,n.b)


class A:
    def __init__(self,name,age):
        self._name=name
        self.__age=age
    @property
    def a(self):
        return self._name
    @a.setter
    def a(self,a):
        self._name=a
    @property
    def b(self):
        return self.__age
    @b.setter
    def b(self,b):
        self.__age=b
# m=A("meg",21)
# print(m.a,m.b)
# m.a="meghana"
# print(m.a)
# m.b=25
# print(m.b)


class Bank:
    def __init__(self,name,account,pin):
        self.name=name
        self._account=account
        self.__pin=pin
        self.__balance=0
    @property
    def balance(self):
        pin=int(input("enter pin:"))
        if pin==self.pin:
            return self.__balance
        return None
    @balance.setter
    def balance(self,b):
        self.__balance=b
    @property
    def account(self):
        return self._account
    @property
    def pin(self):
        return self.__pin
# b=Bank("meghana",123456789,2004)
# print(b.balance,b.account,b.pin)
# b.balance=25
# print(b.balance)


# 1
class BankAccount:
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,nb):
        if nb>=0:
            self.__balance=nb
        else:
            print("invalid balance")
    def deposit(self,amount):
        if amount>0:
            self.__balance=self.__balance+amount
            print("amount deposited")
        else:
            print("invalid amount")
    def withdraw(self,amount):
        if amount>0 and self.__balance-amount>=0:
            self.__balance=self.__balance-amount
        else:
            print("withdraw unsuccessful")
b=BankAccount(123445556,10000)
print("1st question output")
print(b.balance)
b.deposit(1000)
print(b.balance)
b.withdraw(2000)
print(b.balance)
b.withdraw(10000)
print(b.balance)
b.withdraw(-1000)
print(b.balance)



# 2
class Student:
    def __init__(self,name,marks):
        self._name=name
        self.__marks=marks
    @property
    def get_n(self):
        return self._name
    @property
    def get_m(self):
        return self.__marks
    @get_n.setter
    def get_n(self,n):
        self._name=n
    @get_m.setter
    def get_m(self,m):
        if 0<=m<=100:
            self.__marks=m
        else:
            print("invalid marks")
s=Student("meg",87)
print("2nd question output")
print(s.get_n,s.get_m)
s.get_n="meghana"
print(s.get_n)
s.get_m=55
print(s.get_m)
s.get_m=123
print(s.get_m)


# 3
class SecureFile:
    def __init__(self,content,password):
        self.__content=content
        self.__password=password
        self.__log=[]
    @property
    def content(self):
        return self.__content
    @content.setter
    def content(self,nc):
        self.__content=nc
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,np):
        self.__password=np
    def read(self,password):
        if password==self.__password:
            return self.__content
        else:
            self.__log.append("unauthorized attempt")
            return "access denied"
f=SecureFile("secret file",1234)
print("3rd question output")
print(f.content,f.password)
f.content="new file"
print(f.content)
f.password=5678
print(f.password)


# 4
class Employee:
    def __init__(self,salary):
        self.__salary=salary
        self.log=[]
    @property
    def get_salary(self):
        self.log.append("attempt")
        return self.__salary
    @get_salary.setter
    def get_salary(self,salary):
        if self.__salary<salary:
            self.__salary=salary
        else:
            print("invalid")
s=Employee(50000)
print("4th question output")
print(s.get_salary)
s.get_salary=60000
print(s.get_salary)
s.get_salary=20000
print(s.get_salary)


#  5
class product:
    def __init__(self,price,discount):
        self.__price=price
        self.__discount=discount
    @property
    def cost(self):
        return self.__price
    @cost.setter
    def cost(self,price):
        if price>=0:
            self.__price=price
        else:
            print("invalid")
    @property
    def offer(self):
        return self.__discount
    @offer.setter
    def offer(self,discount):
        if 0<=discount<=70:
            self.__discount=discount
        else:
            print("no discount")
    def __final_cost(self):
         fc=self.cost*(1-self.offer/100)
         return fc
    @property
    def final_price(self):
        return self.__final_cost()
p=product(2000,30)
print("5th question output")
print(p.final_price)


#  6
class character:
    def __init__(self,health):
        self.max_limit=self.__health=health
    @property
    def hp(self):
        return self.__health
    def damage(self,points):
        dm=self.__health-points
        if dm>=0:
            self.__health-=points
        else:
            self.__health=0
    def heal(self,points):
        h=self.__health+points
        if h>=self.max_limit:
            self.__health+=points
        else:
            self.__health=self.max_limit
ch=character(200)
print("6th question output")
print(ch.hp)
ch.damage(100)
print(ch.hp)
ch.damage(250)
print(ch.hp)
ch.heal(500)
print(ch.hp)


#  7
class engine:
    def __init__(self):
        self.__temperature=250
    @property
    def temp(self):
        return self.__temperature
    @temp.setter
    def temp(self,nt):
        if 0<=nt<=100:
            self.__temperature=nt
        else:
            self.__temperature=100
class car:
    def __init__(self):
        self.__engine=engine()
        self.start=False
    def dispaly(self):
        print(f"car{'start' if self.start else 'off'}")
        print(f"engine temp:{self.__engine.temp}c")
    def start_car(self):
        if not self.start:
            self.start=True
            self.__engine.temp+=50
        self.dispaly()
    def stop_car(self):
        if self.start:
            self.start=False
            self.__engine.temp-=20
        self.dispaly()
    def cool_engine(self):
        self.__engine.temp-=20
        self.dispaly()
c=car()
print("7th question output")
c.start_car()
c.cool_engine()
c.stop_car()


# 8
class shoppingcart:
    def __init__(self):
        self.__items=[]
    @property
    def items(self):
        return self.__items
    @items.setter
    def items(self,ni):
        print("not modified")
    def add(self,item):
        self.__items.append(item)
    def remove(self,item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            print("not found")
s=shoppingcart()
print("8th question")
s.add("kitkat")
print(s.items)
s.add("munch")
print(s.items)
s.remove("hii")
print(s.items)
s.add("dairymilk")
print(s.items)
s.remove("dairymilk")
print(s.items)


# 9
# incorrectly first
class Attendance:
    def __init__(self):
        self.attendance=[]
    def marks(self,name):
        self.attendance.append(name)
a=Attendance()
print("9th question")
a.marks("meghana")
print(a.attendance)
a.attendance.append("meg")
print(a.attendance)

# correct
class Attendance:
    def __init__(self):
        self.__attendance=[]
    @property
    def attendance(self):
        return self.__attendance
    def mark(self,name):
        return self.__attendance.append(name)
    def remove(self,name):
        if name in self.attendance:
            self.__attendance.remove(name)
a=Attendance()
a.mark("k.meghana")
a.mark("roshini")
print(a.attendance)
a.remove("roshini")
print(a.attendance)


# 10
# we take an example
class student:
    def __init__(self,marks):
        self.__marks=marks
    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self,nm):
        if 0<=nm<=100:
            self.__marks=nm
        else:
            print("invalid marks")
s=student(89)
print("10th question output")
print(s.marks)
s.marks=79
print(s.marks)

# when we forgetting to use underscore prefix, There is no protection because:self.marks is a normal public attribute. So outside code can directly gives output
# example:  self.marks=-89    it gives output as -89

# if we implement a setter without validation Even though __marks is private, the setter allows any value because there is no validation.
# example:  self.__marks=-87  it gives output as -87 but by using validation the output is invalid marks