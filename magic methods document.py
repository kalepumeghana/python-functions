# 1
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def dispaly(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"marks:{self.marks}")
s1=Student("meghana",21,80)
s1.dispaly()

# 2
class BankAccount:
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(self.balance)
b=BankAccount("meghana",2334)
b.deposit(1000)

# 3
class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def inc_salary(self,amount):
        self.salary=self.salary+amount
        print(self.salary)
e1=Employee(1,"meghana",30000)
e1.inc_salary(5000)

# 4
class Employee:
    company="infosys"
    @classmethod
    def change(cls,nc):
        cls.company=nc
print(Employee.company)
Employee.change("tcs")
print(Employee.company)


# 5
class Bank:
    name="sbi"
    @classmethod
    def change(cls,nb):
        cls.name=nb
print(Bank.name)
Bank.change("axis")
print(Bank.name)


# 6
class Hospital:
    name="city hospital"
    @classmethod
    def update(cls,nh):
        cls.name=nh
print(Hospital.name)
Hospital.update("appolo")
print(Hospital.name)


# 7
class Voting:
    @staticmethod
    def is_eligible(age):
        if age>=18:
            print("Eligible to Vote")
        else:
            print("Not Eligible")
v1=Voting.is_eligible(86)
v2=Voting.is_eligible(12)


# 8
class MovieTicket:
    @staticmethod
    def ticket_price(age):
        if age<=12:
            return 100
        elif 12<=age<=60:
            return 200
        else:
            return 150
m=print(MovieTicket.ticket_price(900))
m1=print(MovieTicket.ticket_price(53))
m2=print(MovieTicket.ticket_price(12))


# 9
class DeliveryService:
    @staticmethod
    def delivery_charge(amount):
        if amount>=500:
            print("Free Delivery")
        else:
            print("Delivery charge")
d=DeliveryService.delivery_charge(32)
d1=DeliveryService.delivery_charge(545)
