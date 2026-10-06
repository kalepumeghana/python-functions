# 1
l=[1,2,3,4,5,6,7,8,9]
even=[i for i in l if i%2==0]
print(even)


# 2
l=[1,2,3,4,5]
square=[i*i for i in l]
print(square)


# 3
l=[40,50,30,70,35]
result=["pass" if i>=40 else "fail" for i in l]
print(result)


# 4
num=[10,15,10,20,25,20,30,35,30]
a={i for i in num if i%2==0}
print(a)


# 5
words = ["Python", "Java", "C", "Django", "Python"]
a={len(i) for i in words}
print(a)


# 6
students = {"Rahul": 75,"Anil": 32,"Priya": 56,"Sneha": 28}
a={name:"pass" if marks>=40 else "fail" for name,marks in students.items()}
print(a)


# 7
usernames = ["charan", "rahul", "priya", "sneha"]
passwords = ["abc123", "xyz456", "pqr789", "hello123"]
d={name:password for name,password in zip(usernames,passwords)}
print(d)


# 8
products = {"Laptop": 65000,"Mouse": 500,"Keyboard": 1500,"Monitor": 12000}
p={name:"expensive" if price>10000 else "affordable" for name,price in products.items()}
print(p)


# 9
students = {"Rahul": 35,"Anil": 72,"Priya": 81,"Sneha": 29,"Kiran": 65}
s={name:marks for name,marks in students.items() if marks>=40}
print(s)


# 10
l=(i*i for i in range(1,11))
print(next(l))
print(next(l))
print(next(l))


# 11
even=(i for i in range(1,21) if i%2==0)
for i in even:
    print(i)


# 12
numbers = [10, 15, 20, 25, 30, 35]
gt=[i for i in numbers if i>=20]
print(gt)


# 13
student = {"Rahul": 85,"Anil": 32,"Priya": 76,"Sneha": 45,"Kiran": 28}
d={name:"dictinction" if marks>=75 else "pass" if marks>=40 else "fail" for name,marks in student.items()}
print(d)


# 14
usernames = ["admin", "charan", "root", "guest", "developer"]
v={i:"valid" if len(i)>=5 else "invalid" for i in usernames}
print(v)


# 15
names = ["Rahul", "Priya", "Kiran", "Sneha"]
marks = [75, 35, 82, 28]
r={names[i]:"pass" if marks[i]>=40 else "fail" for i in range(len(names))}
print(r)


