#                                          STR AND REPR
class Employee:
    def __init__(self,n,sal,ex):
        self.name=n
        self.salary=sal
        self.experience=ex
    def __str__(self):
        return f"Name:{self.name}"
e1=Employee("e1",50000,2)
e2=Employee("meghana",30000,1)
print(e1)
print(e2)


class Theater:
    def __init__(self,m,t):
        self.movie=m
        self.tickets=t
        self.tickets_booked=0
    def booking(self,t):
        self.tickets_booked+=t
    def __str__(self):
        k=f'''movie:{self.movie} tickets remaining:{self.tickets-self.tickets_booked}'''
        return k
    def __repr__(self):
        return self.movie
t1=Theater("varanasi",50)
t1.booking(10)
print(t1)
t2=Theater("python",20)
t2.booking(5)
print(t2)
l=[t1,t2]
print(l)
print(repr(t1))


class Inventory:
    def __init__(self):
        self.items=[]
    def add(self,items:list):
        self.items.extend(items)
    def __str__(self):
        return f"items:{self.items}\nTotal:{len(self.items)}"
    def __repr__(self):
        return f"{len(self.items)}"
i1=Inventory()
i2=Inventory()
i3=Inventory()
i1.add(["milk","cake"])
i2.add(["mango","pepsi","sprite"])
i3.add(["kitkat","dailry milk","fivestar","munch"])
print(i2)
l=[i1,i2,i3]
print(l)
print(repr(i3))


# CREATE A STUDENT CLASS WITH NAME,SECTION,MATHS,PHYSICS,CHEMISTRY AS ATTRIBUTES. AN INSTANCE METHOD TO CALCULATE TOTAL
# MARKS AND RETURN THEM. AN INSTANCE/STATC METHOD PROVIDE GRADE LIKE 'A','B','C','D','E','F' BASED ON MARKS
#   SI IS STUDENT CLASS OBJECT
#         PRINT(S1)--NAME:
#                    TOTAL MARKS:                             L=[S1,S2,S3]
#                    GRADE:                                   PRINT(L)--[NAME:GRADE]

class Student:
    def __init__(self,name,section,maths,physics,chemistry):
        self.name=name
        self.section=section
        self.maths=maths
        self.physics=physics
        self.chemistry=chemistry
    def total(self):
        return self.maths+self.physics+self.chemistry
    @staticmethod
    def grade(k):
        if k>=90:
            return 'A'
        elif k>=70:
            return 'B'
        elif k>=60:
            return 'C'
        elif k>=50:
            return 'D'
        elif k>=40:
            return 'E'
        else:
            return 'F'
    def __str__(self):
        s=f'''Name:{self.name} Total:{self.total()} Grade:{self.grade(self.total())}'''
        return s
    def __repr__(self):
        return f"{self.name}:{self.grade(self.total())}"
s1=Student("sita",'A',99,87,76)
s2=Student("reena",'B',95,82,76)
s3=Student("vijay",'C',100,89,90)
print(s1)
l=[s1,s2,s3]
print(l)

# CREATE A CLASS BANK WITH NAME,ACCOUNT,PIN AND BALANCE=0 AS INSTANCE ATTRIBUTES. CREATE WITHDRAW,DEPOSIT,CHANGE_PIN
# METHODS APPLY VALIDATION FOR BOTH WITHDRAW AND CHNAGE_PIN
# B1 AS BANK CLASS OBJECT
#       PRINT(B1)--ENTER PIN:
#                  IF TRUE:                              L=[B1,B2,B3]
#                       DETAILS                          PRINT(L)--[NAME]
#                  ELSE:
#                       WRONG PIN

# class Bank:
#     def __init__(self,name,account,pin):
#         self.name=name
#         self.account=account
#         self.pin=pin
#         self.balance=0
#     def valid_pin(self):
#         p=int(input("Enter your pin:"))
#         return p==self.pin
#     def deposit(self):
#         m=int(input("enter deposit money:"))
#         if m>=0:
#             self.balance+=m
#         else:
#             print("invalid")
#     def withdraw(self):
#         if self.valid_pin():
#             m=int(input("enter your pin:"))
#             if 0<m<self.balance:
#                 print("withdraw successfull")
#                 self.balance-=m
#             else:
#                 print("insufficient money")
#         else:
#             print("wrong pin")
#     def change_pin(self):
#         if self.valid_pin():
#             p=int(input("enter new pin:"))
#             self.pin=p
#             print("pin changed successfully")
#         else:
#             print("wrong password")
#     def __str__(self):
#         if self.valid_pin():
#             return f"Name:{self.name}\naccount no:{self.account}\nbalance:{self.balance}"
#         else:
#             print("wrong pin")
#     def __repr__(self):
#         return self.name
# b1=Bank("megha",844574897548,2005)
# b2=Bank("file",773895785745,45850)
# b3=Bank("hii",85665655766,59585)
# b1.deposit()
# b1.withdraw()
# print(b1)
# l=[b1,b2,b3]
# print(l)
#                                         ARITHMETIC OPERATORS

class Student:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self, o2):
        return self.marks+o2.marks
    def __sub__(self, o2):
        return self.marks-o2.marks
    def __mul__(self, o2):
        return self.marks*o2.marks
    def __truediv__(self, o2):
        return self.marks/o2.marks
    def __mod__(self, o2):
        return self.marks+o2.marks
s1=Student(90)
s2=Student(30)
print(s1+s2)
print(s1-s2)
print(s1*s2)
print(s1/s2)
print(s1%s2)


# class Bank:
#     def __init__(self,account,pin):
#         self.account=account
#         self.pin=pin
#         self.balance=0
#     def valid_pin(self):
#         p=int(input("enter your pin:"))
#         return p==self.pin
#     def __add__(self, o2):
#         if o2>=0:
#             self.balance+=o2
#             return "deposited successfull"
#         else:
#             return "insufficient money"
#     def __sub__(self, o2):
#         if self.valid_pin():
#             if 0<=o2<=self.balance:
#                 self.balance-=o2
#                 return "withdraw succesfull"
#             else:
#                 return "insufficient"
#         else:
#             return "wrong pin"
# b1=Bank(10054,2005)
# print(b1+5000)
# print(b1-2500)

# CREATE A CLASS VECTOR WITH X & Y AS ATTRIBUTES AND V1=VECTOR(7,8)                     PRINT(V1)--VECTOR(7,8)
#                                                    V2=VECTOR(6,7)                     L=[V1,V2]
#                                                    PRINT(V1+V2)                       PRINT(L)--[(7,8),(6,7)]
#                                                    PRINT(V1-V2)

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, o2):
        return (self.x+o2.x,self.y+o2.y)
    def __sub__(self, o2):
        return (self.x-o2.x,self.y-o2.y)
    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return f"({self.x},{self.y})"
v1=Vector(7,8)
v2=Vector(6,7)
print(v1+v2)
print(v1-v2)
print(v1)
l=[v1,v2]
print(l)

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, o2):
        return Vector(self.x+o2.x,self.y+o2.y)
    def __sub__(self, o2):
        return Vector(self.x-o2.x,self.y-o2.y)
    def __str__(self):
        return f"Vector({self.x},{self.y})"
    def __repr__(self):
        return f"Vector({self.x},{self.y})"
v1=Vector(7,8)
v2=Vector(6,7)
v3=Vector(3,4)
print(v1+v2+v3)
print(v1-v2-v3)
v4=v1+v2+v3
print(v4)


class Inv:
    def __init__(self,l=[]):
        self.l=l
    def __add__(self, o2):
        if isinstance(o2,Inv):
            l=self.l+o2.l
            return Inv(l)
        elif isinstance(o2,list):
            self.l.extend(o2)
            return self
        else:
            self.l.append(o2)
            return self
    def __str__(self):
        return f"{self.l}"
i1=Inv()
i1+"Bread"+"kinder joy"+"pen"
i2=Inv()
i2+"soya"+"garam masala"
i3=i1+i2
# i4=i1+["rice","maggie","egg"]
print(i3)
print(i1)
print(i2)
# print(i4)


#                                                GT,GE,LT,LE,NE,EQ
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __gt__(self, o2):
        return self.x>o2.x and self.y>o2
    def __lt__(self, o2):
        return self.x>o2.x and self.y>o2
    def __ne__(self, o2):
        return self.x!=o2.x and self.y!=o2.y
v1=Vector(5,6)
v2=Vector(9,8)
print(v1!=v2)


#                                                EQ,HASH
class Student:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks
    def __gt__(self, o2):
        return self.marks>o2.marks
    def __lt__(self, o2):
        return self.marks<o2.marks
    def __eq__(self, o2):
        return self.marks==o2.marks
    def __hash__(self):
        return hash(self.id)
    def __repr__(self):
        return self.name
s1=Student(60,"meghana",90)
s2=Student(60,"sita",95)
s={s1,s2}
print(s)
print(s2>s1)
print(s1<s2)
# in dictionary(like s={s1,s2}) we use both eq and hash ,when we use only eq or only hash it gives errors.


#                                          LEN , CONTAINS
class Inventory:
    def __init__(self,l=[]):
        self.l=l
    def __len__(self):
        return len(self.l)
    def __add__(self, other):
        if isinstance(other,Inventory):
            l=self.l+other.l
            return Inventory(l)
        else:
            self.l.append(other)
            return self
    def __contains__(self, other):
        return other in self.l
i1=Inventory()
i2=Inventory()
i1+"milk"+"bread"
print(len(i1))
print(len(i1+i2))



