# 1
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def __str__(self):
        return f"{self.title} by {self.author} - Rs.{self.price}"
    def __repr__(self):
        return f"Book('{self.title}','{self.author}','{self.price}')"
b1=Book("nature","mine",900)
print(b1)
print(str(b1))
print(repr(b1))
print(f"{b1}")
print(f"{b1!r}")


# 2
class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return self.x+other.x,self.y+other.y
    def __sub__(self, other):
        return self.x-other.x,self.y-other.y
    def __mul__(self, other):
        return self.x*other.x,self.y*other.y
    def __truediv__(self, other):
        return self.x/other.y,self.y/other.y
    def __floordiv__(self, other):
        return self.x//other.x,self.y//other.y
    def __mod__(self, other):
        return self.x%other.x,self.y%other.y
    def __str__(self):
        return f"({self.x},{self.y})"
v1=Vector2D(3,4)
v2=Vector2D(1,2)
print(v1+v2)
print(v1-v2)
print(v1*v2)
print(v1/v2)
print(v1//v2)
print(v1%v2)
print(repr(v1+v2))


# 3
class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    def __le__(self, other):
        return self.celsius<other.celsius
    def __gt__(self, other):
        return self.celsius>other.celsius
    def __ge__(self, other):
        return self.celsius>=other.celsius
    def __eq__(self, other):
        return self.celsius==other.celsius
    def __hash__(self):
        return hash(self.celsius)
    def __str__(self):
        return f"{self.celsius}"
    def __repr__(self):
        return f"Temperature:{self.celsius}"
t1=Temperature(100)
t2=Temperature(95)
t3=Temperature(105)
print(t1>t2)
print(t1==t2)
print(t1<t3)
t=[t1,t2,t3]
t.sort()
print(t)
t={t1,t2,t3}
print(t)


# 4
class Library:
    def __init__(self,books):
        self.books=books
    def __len__(self):
        return len(self.books)
    def __contains__(self, item):
        return item in self.books
    def __str__(self):
        return f"Library with {len(self.books)} books"
l1=Library(["python","css","html"])
print(len(l1))
print("java" in l1)
print("python" in l1)
print(l1)
print(bool(l1))
empty = Library([])
print(len(empty))
print(bool(empty))


# 1
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __add__(self, other):
        return self.price+other.price
p1=Product("keyboard",1500)
p2=Product("Mouse",700)
print(p1+p2)


#2
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def __sub__(self, other):
        return self.balance-other.balance
b1=BankAccount(10000)
b2=BankAccount(3500)
print(b1-b2)


# 3
class ShoppingCart:
    def __init__(self,total):
        self.total=total
    def __mul__(self, other):
        return self.total*other
c=ShoppingCart(2500)
print(c*3)


# 4
class Bill:
    def __init__(self,amount):
        self.amount=amount
    def __truediv__(self, other):
        return self.amount/other
b1=Bill(1200)
print(b1/4)


# 5
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self, other):
        return self.marks>other.marks
s1=Student("m",85)
s2=Student("n",72)
print(s1>s2)


# 6
class Student:
    def __init__(self,title,isbn):
        self.title=title
        self.isbn=isbn
    def __eq__(self, other):
        return self.isbn==other.isbn
s1=Student("m","isb205")
s2=Student("n","isb205")
print(s1==s2)


# 10
class Team:
    def __init__(self,name,points):
        self.name=name
        self.points=points
    def __le__(self, other):
        return self.points<=other.points
t1=Team("r",25)
t2=Team("j",30)
print(t1<=t2)