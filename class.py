# WITHOUT USING CLASS VARIABLE
class Room:
    def __init__(self,f,ch,l,ac,b,wifi):
        self.fans=f
        self.chairs=ch
        self.lights=l
        self.ac=ac
        self.branch=b
        self.wifi=wifi
R1=Room(6,50,7,1,1,True)
R2=Room(4,35,6,1,1,True)
print(R1.lights)
print(R2.ac)
print(R2.wifi)

# USING CLASS Variable
class Room:
    company="cvcorp"
    def __init__(self,f,ch,l,ac,b,wifi):
        self.fans=f
        self.chairs=ch
        self.lights=l
        self.ac=ac
        self.branch=b
        self.wifi=wifi
R1=Room(5,60,8,1,1,True)
print(Room.company)
print(R1.company)

class Student:
    Batch="py16"
    def __init__(self,name,age,branch):
        self.name=name
        self.age=age
        self.branch=branch
s1=Student("Meghana",21,"ECE")
print(s1.name)
print(Student.Batch)

# UPDATE CLASS VARIABLES WE USE ONLY CLASS NAME
class Student:
    Batch="py16"
    total=0
    def __init__(self,name,age,branch):
        self.name=name
        self.age=age
        self.branch=branch
        Student.total+=1
s1=Student("Meghana",21,"ECE")
s2=Student("Roshini",19,"BCA")
print(s1.age)
print(s1.total)

# INSTANCE METHOD
class Student:
    Batch=16
    def __init__(self,n,a,b):
        self.name=n
        self.age=a
        self.branch=b
    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Branch:{self.branch}")
s1=Student("Meghana",21,"ECE")
s1.display()
s2=Student("Roshini",19,"BCA")
s2.display()

class Employee:
    company="tech"
    bonus=0.2
    def __init__(self,name,experience,salary):
        self.name=name
        self.experience=experience
        self.salary=salary
    def final_salary(self):
        k=self.salary+(self.salary*self.bonus)
        print(f"final_salary:{k}")
    def change_experience(self,new_v):
        self.experience=new_v
        self.display()
    def display(self):
        print(f"Name:{self.name}")
        print(f"Experience:{self.experience}")
        print(f"Salary:{self.salary}")
e1=Employee("Meghana",1,30000)
e1.final_salary()
e1.display()
e1.change_experience(3)
e1.change_experience(10)

#CREATE A CLASS EMPLOYEE WITH NAME,EXPERIENCE,SALARY,DEPARTMENT.IT HAS A METHOD TO CHECK ELIGIBLE FOR PROMOTION IF AVAIL
# ABLE CALLS ANOTHER METHOD TO PROMOTE THE EMPLOYEE "EMP-MANAGER-HR-ADMIN" AND INCREASE THE SALARY

class Employee:
    def __init__(self,name,exp,sal,dep):
        self.name=name
        self.experience=exp
        self.salary=sal
        self.department=dep
    def eligibility(self):
        if self.experience<5:
            print("Not eligible")
        else:
            self.promotion()
    def promotion(self):
        if self.department.lower()=="emp":
            self.department="manager"
            self.salary+=self.salary*0.15
        elif self.department.lower()=="manager":
            self.department="HR"
            self.salary+=self.salary*0.15
        else:
            self.department="admin"
            self.salary+=self.salary*0.15
    def display(self):
        print(f"Name:{self.name}")
        print(f"Experience:{self.experience}")
        print(f"Salary:{self.salary}")
        print(f"Department:{self.department}")
e1=Employee("Meghana",6,40000,"emp")
e2=Employee("Roshini",7,50000,"hr")
e1.eligibility()
e1.display()
e2.eligibility()
e2.display()

# CLASS METHOD
class Book:
    total_Books=0
    def __init__(self,n,a):
        self.name=n
        self.author=a
        Book.total_Books+=1
    @classmethod
    def creation(cls,n,a):
        if len(n)>=5:
            return cls(n,a)
        else:
            return "this is too short"
    @classmethod
    def update(cls,nt):
        cls.total_Books=nt
        print(f"total_books:{cls.total_Books}")
cls=Book
b1=Book.creation("Python","author")
print(b1.name)
b1.update(12)

# 1
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        return self.marks>40
s1=Student("meghana",60)
s2=Student("girl",35)
if s1.is_passed():
    print(s1.name,"passed")
else:
    print(s1.name,"failed")
if s2.is_passed():
    print(s2.name,"passed")
else:
    print(s2.name,"failed")

# 2
class Employee:
    company_name="TechCorp"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
e1=Employee("Meghana")
print(Employee.company_name)
Employee.change_company("MNC")
print(Employee.company_name)

# 3
class MathOps:
    @staticmethod
    def is_even(num):
        return num%2==0
# calling using class
print(MathOps.is_even(2))
# calling using instance
m1=MathOps()
print(m1.is_even(5))

# 4
class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    def display_specs(self):
        print(f"mileage:{self.mileage}")
        print(f"wheels:{self.wheels}")
    @classmethod
    def change(cls,nw):
        cls.wheels=nw
        print(f"wheels:{cls.wheels}")
c1=Car(20)
c1.display_specs()
c2=Car(50)
c2.display_specs()
c1.change(5)
c1.display_specs()
c2.display_specs()

# 5
class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    @staticmethod
    def to_fahrenheit(celsius):
            return (celsius * 9 / 5) + 32
    def show_conversion(self):
        print("Celsius:", self.celsius)
        print("Fahrenheit:", self.to_fahrenheit(self.celsius))
t=Temperature(30)
t.show_conversion()

# 6
class Book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        Book.total_books+=1
    @classmethod
    def from_string(cls,book_str):
        title,author=book_str.split("-")
        if Book.is_valid_title(title):
            return Book(title,author)
        else:
            print("invalid")
    @staticmethod
    def is_valid_title(title):
        return len(title)>=3
title,author=input().split("-")
if Book.is_valid_title(title):
    b1=Book(title, author)
    print(title)
    print(author)
b2=Book.from_string("python-leo")
if b2:
    print(b2.title)
    print(b2.author)
print(Book.total_books)


# 7
class Employee:
    bonus_rate=0.1
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def final_salary(self):
        k=self.base_salary+(self.base_salary*self.bonus_rate)
        print(f"final salary:{k}")
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate=new_rate
    @staticmethod
    def is_valid_salary(sal):
        return sal>1000
e1=Employee("Meghana",10000)
e2=Employee("Roshini",20000)
e1.final_salary()
e2.final_salary()
Employee.update_bonus(0.5)
e1.final_salary()
e2.final_salary()


# 8
class Course:
    total_students=0
    def __init__(self,student_name):
        self.student_name=student_name
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total(cls):
        print(cls.total_students)
    @staticmethod
    def is_eligible(age):
        return age>=18
s1 = Course("Meghana")
s2 = Course("Rahul")
s3 = Course("Priya")

# Enroll students
s1.enroll()
s2.enroll()
s3.enroll()

# Show total students
Course.show_total()

# Check eligibility
print(Course.is_eligible(20))
print(Course.is_eligible(16))
print(Course.is_eligible(67))

# 9
class BankAccount:
    bank_name="sbi"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        if BankAccount.validate_amount(amount):
            self.balance=self.balance+amount
            print(self.balance)
        else:
            print("invalid balance")
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @staticmethod
    def validate_amount(amount):
        return amount>0
b1=BankAccount("Meghana",1500)
b2=BankAccount("girl",100)
b1.deposit(1000)
b2.deposit(-120)
BankAccount.change_bank_name("axis")
print(BankAccount.bank_name)

# 10
class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>=Student.passing_marks:
            print("pass")
        else:
            print("fail")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if marks>=90:
            print("A")
        elif marks>=75:
            print("B")
        else:
            print("C")
s1=Student("Meghana",95)
s2=Student("Roshini",80)
s3=Student("Geeta",35)
Student.update_passing_marks(35)
print(Student.passing_marks)
s1.grade_category(s1.marks)
s1.result()
s2.grade_category(s2.marks)
s2.result()
s3.grade_category(s3.marks)
s3.result()
Student.update_passing_marks(35)
print(Student.passing_marks)


