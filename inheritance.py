# class User:
#     def __init__(self,us,psd,phno,name,age):
#         self.username=us
#         self.psd=psd
#         self.phno=phno
#         self.name=name
#         self.age=age
#     def login(self):
#         print("logged in")
#     def logout(self):
#         print("logout")
# class Swiggy(User):
#     pass
# s1=Swiggy("meghana",2004,7799196527,"maggi",21)
# s1.login()
# # s1() //error
#
#
# class A:
#     def m1(self):
#         print("Hello")
# class B(A):
#     def m2(self):
#         print("B class")
# b1=B()
# b1.m1()
# b1.m2()
# a1=A()
# a1.m1()
# # a1.m2()   //error
#
#
# class A:
#     def m1(self):
#         print("A class")
# class B(A):
#     def m1(self):
#         print("B class")
# b1=B()
# b1.m1()
# a1=A()
# a1.m1()
#
#
# # 1
# class Bank:
#     def name(self,balance):
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#     def withdraw(self,amount):
#         self.balance=self.balance-amount
#     def check_balance(self):
#         print(self.balance)
#
# class User(Bank):
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def dispaly(self):
#         print(f"name:{self.name}")
#         print(f"balance:{self.balance}")
#
# # u=User("meghana",2000)
# # u.dispaly()
# # u.deposit(100)
#
# # class SBI:
# #     def __init__(self,name,acc_no,pin):
# #         self.name=name
# #         self.acc_no=acc_no
# #         self.pin=pin
# #         self.Balance=0
# #         self.Transactions=[]
# #     def deposit(self,amount):
# #         if amount>=0:
# #             self.Balance+=amount
# #             print(f"{amount} Deposited")
# #             self.Transactions.append(f"{amount} deposited")
# #         else:
# #             print("invalid amount")
# #
# #     def check_balance(self):
# #         pin=int(input("enter the pin: "))
# #         if pin ==self.pin:
# #             print(f"your current balance:{self.Balance}")
# #         else:
# #             print("invalid pin")
# # class UnionBank:
# #     def __init__(self,name,acc_no,pin):
# #         self.name=name
# #         self.acc_no=acc_no
# #         self.pin=pin
# #         self.Balance=0
# #         self.Transactions=[]
# #     def withdraw(self,amount):
# #         pin=int(input("enter the pin:"))
# #         if pin==self.pin:
# #             if 0<=amount<=self.Balance:
# #                 self.Balance-=amount
# #                 print(f"your {amount}rs is withdrawn successfully")
# #                 print(f"remaining balance: {self.Balance}")
# #                 self.Transactions.append(f"{amount} withdrawn")
# #             else:
# #                 print("insufficient balance")
# #         else:
# #             print("invalid pin")
# #     def mini_statement(self):
# #         pin=int(input("enter the pin: "))
# #         if pin==self.pin:
# #             for i,j in enumerate(self.Transactions):
# #                 print(f"{i}.{j}")
# #         else:
# #             print("invalid pin")
# # class ATM(SBI,UnionBank):
# #     def menu(self):
# #         print("1. Deposit 2. Withdraw 3. Check_balance 4. Mini_statement")
# #         self.d={1:self.deposit, 2:self.withdraw, 3:self.check_balance, 4:self.mini_statement}
# #     def transaction(self):
# #         self.menu()
# #         ch=int(input("enter your choice:"))
# #         if ch in self.d:
# #             if ch==1 or ch==2:
# #                 a=int(input("enter the amount: "))
# #                 self.d[ch](a)
# #             else:
# #                 self.d[ch]()
# #         else:
# #             print("wrong choice")
# # a1=ATM("meghana",33232222323,232344)
# # a1.transaction()
from random import choice


# 1
# class Bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#     def withdraw(self,amount):
#         self.balance=self.balance-amount
#     def check_balance(self):
#         print(self.balance)
# class User(Bank):
#     def __init__(self,name,balance):
#         super().__init__(balance)
#         self.name=name
#     def display(self):
#         print(f"name:{self.name}")
#         print(f"balance:{self.balance}")
# b=User("meghana",5000)
# b.display()
# b.deposit(1000)
# b.display()
# b.withdraw(2000)
# b.display()
# b.check_balance()


#2
# class Employee:
#     def __init__(self,name,sal):
#         self.name=name
#         self.sal=sal
#     def display_details(self):
#         print(f"name:{self.name}")
#         print(f"sal:{self.sal}")
# class Manager(Employee):
#     def __init__(self,name,sal,bonus):
#         super().__init__(name, sal)
#         self.bonus=bonus
#     def total_salary(self):
#         return self.sal+(self.sal*self.bonus/100)
#     def display_details(self):
#         # print(f"name:{self.name}")
#         # print(f"sal:{self.sal}")
#         super().display_details()
#         print(f"bonus:{self.bonus}")
#         print(f"total:{self.total_salary()}")
# m=Manager("meghana",30000,100)
# m.display_details()


# 3
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display_marks(self):
#         print(f"name:{self.name}")
#         print(f"marks:{self.marks}")
# class Result(Student):
#     def __init__(self,name,marks):
#         super().__init__(name, marks)
#     def result(self):
#         if self.marks>=37:
#             print("passed")
#         else:
#             print("failed")
# s=Result("meg",78)
# s.display_marks()
# s.result()
# s.marks=35
# s.display_marks()
# s.result()


# 4
# class Restaurant:
#     def menu(self,item):
#         if item=="pizza":
#             return 200
#         elif item=="fried rice":
#             return 250
#         elif item=="starters":
#             return 300
#         elif item=="biryani":
#             return 400
#         else:
#             return 0
# class FoodCourt(Restaurant):
#     def display_menu(self):
#         print("1. pizza - 200")
#         print("2. fried rice - 250")
#         print("3. starters - 300")
#         print("4. biryani - 400")
#     def order(self):
#         self.total=0
#         while(True):
#             n=input("enter food item:")
#             m=self.menu(n)
#             if m==0:
#                 print("not available")
#             else:
#                 self.total=self.total+m
#                 print("added:",n)
#             choice=input("do you want anything to add?y/n:")
#             if choice=="n":
#                 break
#     def billing(self):
#         print(f"bill:",self.total)
#         print(f"charge:20")
#         print(f"total bill:",self.total+20)
# class Customer(FoodCourt):
#     pass
# c=Customer()
# c.display_menu()
# c.order()
# c.billing()


# 5
# class Movie:
#     def ticket(self,movie):
#         if movie=="paradise":
#             return 500
#         elif movie=="irumudi":
#             return 400
#         elif movie=="maa inti bangaram":
#             return 300
#         elif movie=="hii":
#             return 200
#         else:
#             return 0
# class Booking(Movie):
#     def movies(self):
#         print("1. paradise - 500")
#         print("2. irumudi - 400")
#         print("3. maa inti bangaram - 300")
#         print("4. hii - 200")
#     def selection(self):
#         self.total=0
#         while(True):
#             n=input("enter movie name:")
#             m=self.ticket(n)
#             if m==0:
#                 print("not available")
#             else:
#                 self.total=self.total+m
#             choice=input("do you want to buy another ticket?y/n:")
#             if choice=="n":
#                 break
#     def billing(self):
#         print("charge : 30")
#         print("total:",self.total+30)
# class Customer(Booking):
#     pass
# c=Customer()
# c.movies()
# c.selection()
# c.billing()


# 6
# class Course:
#     def fee(self,course):
#         if course=="python":
#             return 30000
#         elif course=="java":
#             return 33000
#         elif course=="ai":
#             return 35000
#         elif course=="ml":
#             return 38000
#         elif course=="ai&ml":
#             return 40000
#         else:
#             return 0
# class Academy(Course):
#     def courses(self):
#         print("1.python - 30000")
#         print("2.java - 33000")
#         print("3.ai - 35000")
#         print("4.ml - 38000")
#         print("5.ai&ml - 40000")
#     def enroll(self):
#         self.total=0
#         while(True):
#             n=input("enter the course:")
#             m=self.fee(n)
#             if m==0:
#                 print("not available")
#             else:
#                 self.total=self.total+m
#             choice=input("do you want to add any course?y/n:")
#             if choice=="n":
#                 break
#     def billing(self):
#         print("fee:100")
#         print("total fee:",self.total+100)
# class Student(Academy):
#     pass
#
# s=Student()
# s.courses()
# s.enroll()
# s.billing()


# 11
# class MobileRecharge:
#     def recharge_plans(self):
#         print("1.199 - 1.5gb/day")
#         print("2.299 - 2.0gb/day")
#         print("3.599 - 5.0gb/day")
#     def mobile_recharge(self):
#         n=input("enter mobile number:")
#         plan=input("enter plan:")
#         if plan=="199":
#             print("recharge successful:199")
#         elif plan=="299":
#             print("recharge successful:299")
#         elif plan=="599":
#             print("recharge successful:599")
#         else:
#             print("invalid plan")
# class BusTicket:
#     def display_bus(self):
#         print("1.Hyderabad to Vizag:5000")
#         print("2.Vizag to Vijayawada:3000")
#         print("3.Srikaulam to Hyderabad:10000")
#     def book_ticket(self):
#         a=input("enter bus number:")
#         if a=="1":
#             print("ticket booked from hyd to vsp:5000")
#         elif a=="2":
#             print("ticket booked from vsp to vjz:3000")
#         elif a=="3":
#             print("ticket booked from sklm to hyd:10000")
# class ElectricityBills:
#     def bill_details(self):
#         print("electricity bill:1000")
#     def pay_bill(self):
#         choice=input("do you want the bill?y/n:")
#         if choice=="y":
#             print("electricity bill paid")
#         else:
#             print("bill cancelled")
# class Paytm(MobileRecharge,BusTicket,ElectricityBills):
#     def menu(self):
#         print("1.Mobile recharge")
#         print("2.Bus ticket booking")
#         print("3.electricity bills")
#     def service(self):
#         c=input("enter the menu:")
#         if c=="1":
#             self.recharge_plans()
#             self.mobile_recharge()
#         elif c=="2":
#             self.display_bus()
#             self.book_ticket()
#         elif c=="3":
#             self.bill_details()
#             self.pay_bill()
#         else:
#             print("invalid")
# p=Paytm()
# p.menu()
# p.service()


# 10
# class SBI:
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print("deposit success",amount)
#     def check_balance(self):
#         print("balance:",self.balance)
# class UnionBank:
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance=self.balance-amount
#             print("withdraw:",amount)
#         else:
#             print("insufficient balance")
#     def mini_statement(self):
#         print("mini statement")
#         print("current balance:",self.balance)
# class ATM(SBI,UnionBank):
#     def __init__(self):
#         self.balance=1000
#     def menu(self):
#         print("1.deposit")
#         print("2.check balance")
#         print("3.withdraw")
#         print("4.mini statement")
#     def transaction(self):
#         while(True):
#             self.menu()
#             choice=input("enter your choice:")
#             if choice=="1":
#                 amount=int(input("enter deposit amount:"))
#                 self.deposit(amount)
#             elif choice=="2":
#                 amount=int(input("enter withdraw amount:"))
#                 self.withdraw(amount)
#             elif choice=="3":
#                 self.check_balance()
#             elif choice=="4":
#                 self.mini_statement()
#             else:
#                 print('invalid choice')
#             n=input("do you want to continue?y/n0:")
#             if n=="n0":
#                 break
# a=ATM()
# a.transaction()


##Hierarchical Inheritance###
# 1ST#
class Cab:
    def bike_fare(self,distance):
        return distance*10
    def auto_fare(self,distance):
        return distance*15
    def cab_fare(self,distance):
        return distance*20
class Uber(Cab):
    def menu(self):
        print("1.bike\n2.Auto\n3.Cab")
    def booking(self):
        while True:
            self.menu()
            choice=int(input("Enter:"))
            if choice==1:
                distance=int(input("Enter Distance:"))
                fare=self.bike_fare(distance)
            elif choice==2:
                distance = int(input("Enter Distance:"))
                fare=self.auto_fare(distance)
            elif choice==3:
                distance = int(input("Enter Distance:"))
                fare=self.cab_fare(distance)
            else:
                print("Invalid Choice")
                return
            self.billing(fare)
    def billing(self,fare):
        gst=fare*10/100
        bill=fare+gst
        if bill>1000:
            discount=bill*15/100
            bill=bill-discount
        print("Fare:",fare)
        print("Bill:",bill)
        print("GST:",gst)
class Ola(Cab):
    def menu(self):
        print("1.Bike\n2.Auto\n3.Cab")
    def booking(self):
        self.menu()
        while True:
            choice=int(input("Enter ur choice:"))
            if choice==1:
                distance=int(input("Enter Distance:"))
                fare=self.bike_fare(distance)
            elif choice==2:
                distance=int(input("Enter Distance:"))
                fare=self.auto_fare(distance)
            elif choice==3:
                distance=int(input("Enter Distance:"))
                fare=self.cab_fare(distance)
            else:
                print("Invalid Choice")
                return
            self.billing(fare)
    def billing(self,fare):
        gst=fare*12/100
        bill=fare+gst
        if bill>1500:
            discount=bill*20/100
            bill=bill-discount
        print("Fare:",fare)
        print("GST:",gst)
        print("Total Bill:",bill)
print("1.Uber\n2.Ola")
choice=int(input("Enter ur choice:"))
if choice==1:
    u=Uber()
    u.booking()
elif choice==2:
    o=Ola()
    o.booking()
else:
    print("Invalid Choice")
 # 2nd#
class Grocery:
    def rice_price(self,kg):
        return kg*20
    def sugar_price(self,kg):
        return kg*10
    def Oil_price(self,litre):
        return litre*15
class Dmart(Grocery):
    def items(self):
        print("1.rice\n2.sugar\n3.oil")
    def shopping(self):
        self.items()
        choice=int(input("Enter:"))
        if choice==1:
            kg=int(input("Enter:"))
            value=self.rice_price(kg)
        elif choice==2:
            kg=int(input("Enter:"))
            value=self.sugar_price(kg)
        elif choice==3:
            litre=int(input("Enter:"))
            value=self.Oil_price(litre)
        else:
            print("Invalid Choice")
            return
        self.billing(value)
    def billing(self,value):
        gst=value*5/100
        bill=gst+value
        if bill>2000:
            discount=bill*10/100
            bill=bill-discount
        print("GST:",gst)
        print("Value:",value)
        print("Total Bill:",bill)
class RelianceSmart(Grocery):
    def items(self):
        print("1.rice\n2.sugar\n3.oil")
    def shopping(self):
        self.items()
        choice=int(input("Enter:"))
        if choice==1:
            kg=int(input("Enter:"))
            value=self.rice_price(kg)
        elif choice==2:
            kg=int(input("Enter:"))
            value=self.sugar_price(kg)
        elif choice==3:
            litre=int(input("Enter:"))
            value=self.Oil_price(litre)
        else:
            print("Invalid Choice")
            return
        self.billing(value)
    def billing(self,value):
        gst=value*5/100
        bill=gst+value
        if bill>2500:
            discount=bill*15/100
            bill=bill-discount
        print("GST:",gst)
        print("Value:",value)
        print("Total Bill:",bill)
print("1.DMART\n2.RELIANCESMART")
choice=int(input("Enter ur Choice:"))
if choice==1:
    d=Dmart()
    d.shopping()
elif choice==2:
    r=RelianceSmart()
    r.shopping()
else:
    print("Invalid Choice")
# 3rd#
class Bus:
    def sleeper_fare(self,number):
        return number*100
    def SemiSleeper_fare(self,number):
        return number*200
    def ac_fare(self,number):
        return number*30
class RedBus(Bus):
    def routes(self):
        print("1.Vizag to chennai")
        print("2.Vizag to Goa")
        print("3.Vizag to Bangalore")
    def booking(self):
        self.routes()
        choice=int(input("Enter:"))
        if choice==1:
            number=int(input("Enter:"))
            fare=self.sleeper_fare(number)
        elif choice==2:
            number=int(input("Enter:"))
            fare=self.SemiSleeper_fare(number)
        elif choice==3:
            number=int(input("Enter:"))
            fare=self.ac_fare(number)
        else:
            print("Invalid")
            return
        self.billing(fare)
    def billing(self,fare):
        gst=fare*10/100
        charge=30
        bill=gst+fare+charge
        print("GST:",gst)
        print("FARE:",fare)
        print("TOTAL BILL:",bill)
class AbhiBus(Bus):
    def routes(self):
        print("1.Vizag to chennai")
        print("2.Vizag to Goa")
        print("3.Vizag to Bangalore")
    def booking(self):
        self.routes()
        choice=int(input("Enter:"))
        if choice==1:
            number=int(input("Enter:"))
            fare=self.sleeper_fare(number)
        elif choice==2:
            number=int(input("Enter:"))
            fare=self.SemiSleeper_fare(number)
        elif choice==3:
            number=int(input("Enter:"))
            fare=self.ac_fare(number)
        else:
            print("Invalid")
            return
        self.billing(fare)
    def billing(self,fare):
        gst=fare*10/100
        charge=20
        bill=gst+fare+charge
        print("GST:",gst)
        print("FARE:",fare)
        print("TOTAL BILL:",bill)
print("1.RedBus\n2.AbhiBus")
choice=int(input("Enter your choice:"))
if choice==2:
    a=AbhiBus()
    a.booking()
elif choice==1:
    r=RedBus()
    r.booking()
else:
    print("Invalid Choice")





