# # ELEMENT BASED
# s=("python")
# # for i in s:
# #     print(i)
#
# # INDEX BASED
# for i in range(len(s)):
#     print(s[i])
#
#                                                                # METHODS
#
# # LOWER()
# s1="pYthON"
# s2=s1.lower()
# print("lower")
# print(s2)
# print(s1)
#
# # UPPER()
# s1="javaAA"
# s2=s1.upper()
# print("upper")
# print(s2)
# print(s1)
#
# # SWAPCASE
# s1="PyThoN"
# s2=s1.swapcase()
# print("swapcase")
# print(s2)
# print(s1)
#
# # CAPITALIZE
# s1="my name is meghana"
# s2=s1.capitalize()
# print("capitalize")
# print(s2)
# print(s1)
#
# # TITLE
# s1="my name is meghana"
# s2=s1.title()
# print("title")
# print(s2)
# print(s1)
#
# # COUNT
# s="javaprogramming"
# print("count")
# a=s.count("a")
# print(a)
# b=s.count("a",3)
# print(b)
# c=s.count("p",4,10)
# print(c)
# d=s.count("e",1,15)
# print(d)
# e=s.count("ing")
# print(e)
#
# # FIND
# print("find")
# a=s.find("a")
# print(a)
# b=s.find("r",4)
# print(b)
# c=s.find("g",6,9)
# print(c)
# d=s.find("k")
# print(d)
# e=s.find("gra")
# print(e)
#
# # RFIND
# print("rfind")
# a=s.rfind("g")
# print(a)
# b=s.rfind("a",2,11)
# print(b)
# c=s.rfind("g",1,7)
# print(c)
#
# # INDEX
# print("index")
# a=s.index("a")
# print(a)
# b=s.index("g",6)
# print(b)
# c=s.index("a",2,8)
# print(c)
# # d=s.index("k")
# # print(d)
#
# # RINDEX
# print("rindex")
# a=s.rindex("a")
# print(a)
# b=s.rindex("m",2)
# print(b)
# c=s.rindex("i",2,13)
# print(c)
# # d=s.rindex("k")
# # print(d)
#
# # ENDSWITH
# print("endswith")
# a=s.endswith("ing")
# print(a)
# b=s.endswith("py")
# print(b)
# c=s.endswith("programming")
# print(c)
# d=s.endswith("javaprogramming")
# print(d)
#
# # STARTSWITH
# print("startswith")
# a=s.startswith("java")
# print(a)
# b=s.startswith("pro")
# print(b)
# c=s.startswith("javaprog")
# print(c)
# d=s.startswith("javaprogramming")
# print(d)
#
# # ISALPHA : it consists of only alphabets, it doesn't contain any spaces,special characters, numbers
# s1="javaprogramming"
# s2="py1"
# s3="@py!"
# s4="py thon"
# print("isalpha")
# print(s1.isalpha())
# print(s2.isalpha())
# print(s3.isalpha())
# print(s4.isalpha())
#
# # ISDIGIT : it consists of only numbers
# s1="py16"
# s2="123"
# s3="py"
# print("isdigit")
# print(s1.isdigit())
# print(s2.isdigit())
# print(s3.isdigit())
# print(s4.isdigit())
#
# # ISALNUM : it consists of only numbers, alphabets and both
# s1="py16"
# s2="123"
# s3="py"
# s4="py@1#"
# s5="java pro"
# print("isalnum")
# print(s1.isalnum())
# print(s2.isalnum())
# print(s3.isalnum())
# print(s4.isalnum())
# print(s5.isalnum())
#
# # ISLOWER : it consists of only combination of these small alphabets, numbers,special characters or only small alphabets
# s1="p3@thon"
# s2="pytHon"
# s3="4@5"
# s4="bye"
# print("islower")
# print(s1.islower())
# print(s2.islower())
# print(s3.islower())
# print(s4.islower())
#
# # ISUPPER : it consists of only combination of these capital alphabets, numbers,special characters or only capital letters
# s1="1@JA2VA"
# s2="JAVA"
# s3="123"
# s4="J12ava"
# print("isupper")
# print(s1.isupper())
# print(s2.isupper())
# print(s3.isupper())
# print(s4.isupper())
#
# # ISSPACE
# s1="1@JA2VA"
# s2="JA "
# s3=" "
# print("isspace")
# print(s1.isspace())
# print(s2.isspace())
# print(s3.isspace())
#
# # SPLIT
# s="bcadeabgklafgh"
# l=s.split("a")
# print("split")
# print(*l)
#
# s="python is a pro language"
# l=s.split(" ")
# print(l)
# print(*l)
#
# s="bcdabcaacdefaaklmn"
# l=s.split("a")
# print(l)
# print(*l)
#
# # REPLACE : if there is no word what we want to replace then it prints the same string
# s="python is a pro language"
# s1=s.replace("python","java")
# print("replace")
# print(s1)
#
# s2=s.replace(" ","@")
# print(s2)
#
# s3=s.replace("java","c")
# print(s3)
#
# # STRIP
# s=" python pro language "
# print("strip")
# s1=s.strip()
# print(s1)
#
# # LSTRIP
# s1=s.lstrip()
# print(s1)
#
# s2=s.rstrip()
# print(s2)
#
# # REMOVE PREFIX
# s="python pro language"
# k=s.removeprefix("python")
# print("remove prefix")
# print(k)
#
# l=s.removeprefix("java")
# print(l)
#
# # REMOVE SUFFIX
# print("remove suffix")
# l=s.removesuffix("language")
# print(l)
#
# k=s1.removesuffix("pro")
# print(k)
#
# # JOIN
# s="python"
# l=["hi","bye","python","java"]
# print("join")
# k=",".join(s)
# print(k)
# m="@".join(l)
# print(m)




# 1
# n=input()
# print(len(n))
#
# # 2
# n=input()
# for i in n:
#     print(ord(i))
#
# # 3
# n=input()
# m=n.upper()
# print(m)
#
# # 4
# n=input()
# m=n.lower()
# print(m)
#
# # 5
# n=input()
# m=n.replace(" ","-")
# print(m)
#
# # 6
# n=input()
# print(n.isdigit())

# 7
# n=input()
# print(n.isalpha())

# 8
# n=input()
# print(n.isalnum())

# 9
# n=input()
# if len(n)==14 and n[4]==" " and n[9]==" ":
#     n=n.replace(" ","")
# if len(n)==12 and n.isdigit():
#     print("valid aadhar number")
# else:
#     print("not a valid aadhar number")

# 10
# s=input()
# if len(s)==10:
#     c=0
#     for i in range(len(s)):
#         if(i==0 or i==1 or i==2 or i==4 or i==9) and (s[i].upper()):
#             c=c+1
#         elif(i>=5 and i<=8) and (s[i].isdigit()):
#             c=c+1
#         elif(i==3 and (s[i] in "CHATPF")):
#             c=c+1
#     if c==10:
#         print("valid")
#     else:
#         print("invalid")
# else:
#     print("invalid")


# 12
# s=input()
# if len(s)==9:
#     uc=lc=dc=sc=False
#     sp=True
#     for i in s:
#         if(i.isupper()):
#             uc=True
#         elif(i.islower()):
#             lc=True
#         elif(i.isdigit()):
#             dc=True
#         elif(i!=" "):
#             sc=True
#         else:
#             sp=False
#             break
#     if(uc and lc and dc and sc and sp):
#         print("valid")
#     else:
#         print("invalid")


# 14
# s=input()
# n=input()
# a=s.find(n)
# print(a)


# 15
# s=input()
# n=input()
# a=s.count(n)
# print(a)


# 16
# s=input()
# n=input()
# if n in s:
#     print("word is present")
# else:
#     print("not present")


# 17
# s=input()
# for i in s:
#     if i.isdigit():
#         print(i)


# 18
# s=input()
# a=0
# b=0
# for i in s:
#     if i.islower():
#         a=a+1
#     if i.isupper():
#         b=b+1
# print(a)
# print(b)


# 19
# s=input()
# for i in s:
#     if i.isalpha():
#         print(i,end="")
# print()
# for i in s:
#     if i.isdigit():
#         print(i,end="")
# print()
# for i in s:
#     if i=="!" or i=="@" or i=="#" or i=="%" or i=="^" or i=="&" or i=="*":
#         print(i,end="")


# 20
# s=input()
# for i in range(len(s)-1,-1,-1):
#     print(s[i],end="")


# 21
# s=input()
# t=""
# for i in s:
#     if i!=" ":
#         t=t+i
# rev=""
# for i in range(len(t)-1,-1,-1):
#     rev=rev+t[i]
# if t==rev:
#     print("palindrome")
# else:
#     print("not")


# 22
s=input()
a=s.split()
for i in a:
    print(i[::-1],end="")



