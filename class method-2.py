#1
class Student:
    total_students=0
    passing_marks=40
    curve_marks=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.total_students+=1
    def before_marks(self):
        self.marks=self.marks+(self.marks*Student.curve_marks/100)
        if self.marks>100:
            self.marks=100
    def display(self):
        if self.marks>=Student.passing_marks:
            result="pass"
        else:
            result="fail"
        print(f"name:{self.name}")
        print(f"marks:{self.marks}")
        print(f"result:{result}")
        print(f"grade:{Student.grade(self.marks)}")
    @classmethod
    def update_curve(cls,nw):
        cls.curve_marks=nw
    @staticmethod
    def grade(marks):
        if marks>=90:
            return "A"
        elif marks>=80:
            return "B"
        elif marks>=70:
            return "C"
        elif marks>=60:
            return "D"
        elif marks>=40:
            return "E"
        else:
            return "F"
s1=Student("girl1",90)
s2=Student("girl2",70)
s3=Student("girl3",49)
s1.display()
s2.display()
s3.display()
Student.curve_marks=10
s1.before_marks()
s2.before_marks()
s3.before_marks()
s1.display()
s2.display()
s3.display()

# 2
class Product:
    base_tax_rate=12
    def __init__(self,name,base_price):
        self.name=name
        self.base_price=base_price
        # Product.base_tax_rate+=1
    def final_price(self):
        return self.base_price+(self.base_price*Product.base_tax_rate/100)
    @classmethod
    def change_tax_rate(cls,nt):
        cls.base_tax_rate=nt
    @staticmethod
    def is_valid(price):
        if price>0:
            return True
        else:
            return False
p1=Product("rate1",1000)
p2=Product("rate2",50000)
print(p1.final_price())
print(p2.final_price())
Product.change_tax_rate(20)
print(Product.base_tax_rate)
print(p1.final_price())
print(p2.final_price())
print(Product.is_valid(10000))
print(Product.is_valid(-400))


# 3
class Employee:
    experience=2
    def __init__(self,name,experience,department):
        self.name=name
        self.experience=experience
        self.department=department
    def promotion(self):
        if self.experience>=Employee.experience:
            print("eligible")
        else:
            print("not eligible")
    @classmethod
    def update(cls,ne):
        cls.experience=ne
    @staticmethod
    def is_valid(dept):
        if dept=="HR" or dept=="Tech" or dept=="Admin":
            return True
        else:
            return False
e1=Employee("e1",2,"HR")
e1.promotion()
print(Employee.is_valid("Tech"))
print(Employee.is_valid("other"))
Employee.update(5)
print(Employee.experience)
e1.promotion()


# 4
class Loan:
    interest_rate=10
    def __init__(self,name,principal):
        self.name=name
        self.principal=principal
    def total_amount(self):
        k=self.principal + (self.principal * Loan.interest_rate / 100)
        print(f"total_amount:{k}")
    @classmethod
    def update(cls,ni):
        cls.interest_rate=ni
    @staticmethod
    def is_eligibility(salary):
        if salary>=50000:
            return True
        else:
            return False
l1=Loan("l1",10000)
l1.total_amount()
print(Loan.is_eligibility(50000))
Loan.update(15)
print(Loan.interest_rate)
l1.total_amount()


# 5
class Course:
    total_course=0
    min_duration=20
    def __init__(self,title,duration):
        self.title=title
        self.duration=duration
        self.enrolled_students=0
        Course.total_course+=1
    def enroll_student(self):
        self.enrolled_students+=1
        print(self.title)
        print(self.enrolled_students)
    @classmethod
    def update(cls,nd):
        cls.min_duration=nd
    @staticmethod
    def is_check(duration):
        if duration >=0 and duration <=365:
            return True
        else:
            return False
c1=Course("c1",12)
c2=Course("c2",15)
c3=Course("c3",20)
print(Course.total_course)
c1.enroll_student()
c2.enroll_student()
c3.enroll_student()
print(Course.is_check(c1.duration))
print(Course.is_check(c2.duration))
print(Course.is_check(400))
Course.update(30)
print(Course.min_duration)


# 6
class Vehicle:
    service_charge_rate=10
    def __init__(self,model,kilometers_run,service_history):
        self.model=model
        self.kilometers_run=kilometers_run
        self.service_history=service_history
    def service_charge(self):
        k=self.kilometers_run+(self.kilometers_run*Vehicle.service_charge_rate/100)
        print(f"service_charge:{k}")
    @classmethod
    def update(cls,ns):
        cls.service_charge_rate=ns
    @staticmethod
    def is_check(age):
        if age<=15:
            return True
        else:
            return False
v1=Vehicle("v1",150,3)
v1.service_charge()
print(Vehicle.is_check(20))
print(Vehicle.is_check(10))
Vehicle.update(20)
print(Vehicle.service_charge_rate)


# 7
class Inventory:
    total_items = 0
    minimum_stock = 10
    def __init__(self):
        self.stock = {}
    def update_stock(self, item, quantity):
        if item in self.stock:
            self.stock[item] += quantity
        else:
            self.stock[item] = quantity

        Inventory.total_items += quantity

        print(item, "Stock:", self.stock[item])

        # Using static method inside instance method
        if Inventory.check_stock(self.stock[item]):
            print(item, "is below minimum stock.")
        else:
            print(item, "stock is sufficient.")
    @classmethod
    def update_threshold(cls, new_threshold):
        cls.minimum_stock = new_threshold
    @staticmethod
    def check_stock(stock):
        if stock < Inventory.minimum_stock:
            return True
        else:
            return False
i1 = Inventory()
i2 = Inventory()
i1.update_stock("Pen", 15)
i1.update_stock("Pen", -8)
i2.update_stock("Book", 5)
print("\nTotal Items:", Inventory.total_items)
Inventory.update_threshold(12)
print("New Minimum Stock:", Inventory.minimum_stock)
i1.update_stock("Pen", 0)
i2.update_stock("Book", 0)


# 8
class HotelRoom:
    base_price=1000
    def __init__(self,room_number,nights_booked,guest_name):
        self.room_number=room_number
        self.nights_booked=nights_booked
        self.guest_name=guest_name
    def total_bill(self):
        if HotelRoom.is_check(self.nights_booked):
            k = self.nights_booked * HotelRoom.base_price
            print(f"total_bill:{k}")
        else:
            print("Invalid number of nights.")
    @classmethod
    def update(cls,nb):
        cls.base_price=nb
    @staticmethod
    def is_check(nights_booked):
        if nights_booked>0:
            return True
        else:
            return False
h1=HotelRoom(205,2,"meghana")
h1.total_bill()
print(HotelRoom.is_check(3))
HotelRoom.update(2000)
print(HotelRoom.base_price)
h1.total_bill()
print(HotelRoom.is_check(0))


# 9
class LibraryMember:
    total_active_members = 0
    borrowing_limit = 3
    def __init__(self, name):
        self.name = name
        self.books_borrowed = 0
        LibraryMember.total_active_members += 1
    def borrow_book(self, title):
        if LibraryMember.check_book_title(title):
            if self.books_borrowed < LibraryMember.borrowing_limit:
                self.books_borrowed += 1
                print(self.name, "borrowed", title)
                print("Books Borrowed:", self.books_borrowed)
            else:
                print(self.name, "has reached the borrowing limit.")
        else:
            print("Invalid Book Title")
    @classmethod
    def update_limit(cls, new_limit):
        cls.borrowing_limit = new_limit
    @staticmethod
    def check_book_title(title):
        if len(title) > 0:
            return True
        else:
            return False
m1 = LibraryMember("Meghana")
m2 = LibraryMember("Rahul")
print("Total Active Members:", LibraryMember.total_active_members)
m1.borrow_book("Python")
m1.borrow_book("Java")
m1.borrow_book("C")
m1.borrow_book("HTML")
m2.borrow_book("Data Science")
m2.borrow_book("")
LibraryMember.update_limit(5)
print("\nUpdated Borrowing Limit:", LibraryMember.borrowing_limit)
m1.borrow_book("HTML")
print("\nValidation:")
print(LibraryMember.check_book_title("Python"))
print(LibraryMember.check_book_title(""))


# 10
class Member:
    bmi_limit = 25
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def check_fit(self):
        if Member.check_input(self.height, self.weight):
            k = self.weight / (self.height ** 2)
            print(f"check_fit:{round(k,2)}")
            if k <= Member.bmi_limit:
                print("Fit")
            else:
                print("Not Fit")
        else:
            print("Invalid height or weight")
    @classmethod
    def update_bmi_limit(cls, nl):
        cls.bmi_limit = nl
    @staticmethod
    def check_input(height, weight):
        if height > 0 and weight > 0:
            return True
        else:
            return False
m1 = Member("Meghana", 1.6, 55)
m2 = Member("Rahul", 1.7, 80)
m3 = Member("Priya", -1.5, 50)
m1.check_fit()
m2.check_fit()
m3.check_fit()
Member.update_bmi_limit(30)
print(Member.bmi_limit)
m1.check_fit()
m2.check_fit()
print(Member.check_input(1.8, 70))
print(Member.check_input(-1.6, 60))