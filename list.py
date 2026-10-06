# # APPEND
# l=[1,2,3,4,5]
# print(l)
# print(*l)
# l.append(6)
# l.append([7,8])
# print(l)
# print(*l)
#
# #  EXTEND
# l=[1,2,3,4,5]
# l1=[6,7,8]
# l.extend(l1)
# l.extend("meghana")
# print(l)
# print(*l)
#
# # INSERT
# l=[1,2,3,4,5]
# l.insert(2,0)
# l.insert(7,9)
# print(*l)
#
# # REMOVE
# l=[1,2,3,4,5]
# l.remove(2)
# # l.remove(9)  //ERROR
# print(*l)
#
# # POP
# l=[1,2,3,4,5]
# n=l.pop(3)
# print(*l)
# print(n)
# l=[1,2,3,4,5]
# k=l.pop()
# print(*l)
# print(k)
#
# # CLEAR
# l=[1,2,3,4,5]
# l.clear()
# print(l)
#
# # INDEX
# l=[1,2,3,4,5,1,2,3,5]
# print(l.index(5))
# print(l.index(3,2))
# print(l.index(2,3,7))
# # print(l.index(100)) //error
#
# # COUNT
# l=[1,2,3,4,5,5,2,1,4,4,4]
# c=l.count(4)
# m=l.count(5)
# print(c)
# print(m)
#
# # SORT
# l=[5,7,9,4,3]
# l.sort()    #default it takes reverse==False it means ascending order
# print(l)
# m=[10,608,93767,947]
# m.sort(reverse=True)
# print(m)
#
# #REVERSE
# l=[5,6,7,8,9]
# l.reverse()
# print(l)
#
# # COPY
# l=[1,2,3,4,5]
# # l1=l.copy()
# print(l.copy())
#
# l=[10,20,30,40,50]
# n=l.pop(2)
# print(*l)
#
# l=[50,60,70,80]
# l.insert(2,90)
# l.remove(60)
# print(l)
#
# m=[11,22,33,44,55]
# n=m.pop(4)
# print(*m)
# print(n)
#
# a=[9,8,7,6,5,7,9,4,6,7]
# print(a.index(8))
# print(a.index(6,7))
# print(a.index(7,2,8))
from string import digits
from unittest import result

# 2
# l=[1,2,3,4,5]
# m=l.insert(2,6)
# print(l)
# # 3
# l=[1,2,3,4,5]
# m=l.append([6,7])
# print(l)
# # 4
# l=[6,7,8,9]
# l.remove(8)
# print(l)
# # 5
# l=[1,2,3,4,5]
# n=l.pop(3)
# print(l)
# # 6
# l=[10,20,30,40,50]
# print(l.index(50))
# # 7
# l=[1,1,3,3,3,3,4,6,6,6,7]
# print(l.count(6))
# # 13
# l=[9,8,7,6,5]
# l.reverse()
# print(l)
# # 8
# l=[1,2,3,4,5]
# a=l[1]+l[-1]
# print(a)
# # 9
# l=[5,6,7,8,9]
# a=sum(l[:2+1])
# print(a)
# # 10
# l=[1,2,3,4,5,6,7]
# sum=0
# c=0
# for i in l:
#     if i%2==1:
#         sum=sum+i
#         c=c+1
# print(sum//c)
# # 11
# l=[2,4,5,8,9,11,43,89,66]
# a=[]
# for n in l:
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc=fc+1
#     if fc==2:
#         a.append(n)
# print(a)

# l=[10,20,30,40,50,60]
# print(l[1:5:1])
# print(l[2:5])
# print(l[2])
# print(l[:])
# print(l[0:6:2])
# print(l[4:1:1])
# print(l[1:4:-1])
#
# print(l[5:1:-1])
# print(l[-5:4:1])
# print(l[-5:-1:1])
# print(l[-1:2:1])
#
# print(l[0:7])
# print(l[4:-7:-1])
# print(l[-2:1:-1])
# print(l[len(l)-1:-7:-1])
# print(l[:-7:-1])
# print(l[::-1])


#   ANTI-CLOCK WISE ROTATION
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     print(*l)
#     l=l[1:len(l)]+[l[0]]


#   ANTI-CLOCK WISE ROTATION K TIMES
# l=list(map(int,input().split()))
# k=int(input())
# for i in range(k):
#     l=l[1:len(l)]+[l[0]]
# print(*l)

#   ANTI-CLOCK WISE ROTATION WITHOUT USING PREDEFINED FUNCTIONS
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     k=l[0]
#     print(*l)
#     for j in range(1,len(l)):
#         l[j-1]=l[j]
#     l[len(l)-1]=k


#   ANTI-CLOCK WISE ROTATION K TIMES WITHOUT USING PREDEFINED FUNCTIONS
# l=list(map(int,input().split()))
# k=int(input())
# for i in range(k):
#     k=l[0]
#     for j in range(1,len(l)):
#         l[j-1]=l[j]
#     l[len(l)-1]=k
# print(*l)


#   CLOCK WISE ROTATION
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     print(*l)
#     l=[l[len(l)-1]]+l[0:len(l)-1]


# CLOCK WISE ROTATION K TIMES
# l=list(map(int,input().split()))
# k=int(input())
# for i in range(k):
#     l=[l[len(l)-1]]+l[0:len(l)-1]
# print(*l)


# CLOCK WISE ROTATION WITHOUT USING PREDEFINED FUNCTIONS
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     print(*l)
#     k=l[len(l)-1]
#     for j in range(len(l)-1,0,-1):
#         l[j]=l[j-1]
#     l[0]=k


#   CLOCK WISE ROTATION K TIMES WITHOUT USING PREDEFINED FUNCTIONS
# l=list(map(int,input().split()))
# k=int(input())
# for i in range(k):
#     a=l[len(l)-1]
#     for j in range(len(l)-1,0,-1):
#         l[j]=l[j-1]
#     l[0]=a
# print(*l)

# KTH NEIGHBOUR
# n = int(input("Enter a number: "))
# # Step 1: Check whether the number has at least 2 digits
# if n < 10:
#     print("Invalid Input")
# else:
#     # Step 2: Convert the number into individual digits
#     digits = []
#     for i in str(n):
#         digits.append(int(i))
#     # Step 3: Find how many digits are present
#     count = len(digits)
#     # Step 4: Keep generating new numbers
#     while True:
#         total = 0
#         # Step 5: Add the previous 'count' numbers
#         for i in digits[-count:]:
#             total = total +  i
#         # Step 6: Check whether the new number is equal to n
#         digits.append(total)
#         if total == n:
#             print("Keith Number")
#             break
#         # Step 7: If the new number becomes bigger than n,
#         # it can never come back down
#         if total > n:
#             print("Not a Keith Number")
#             break


# r=int(input())
# c=int(input())
# l=[]
# for i in range(r):
#     k=list(map(int,input().split()))
#     l.append(k)
# for i in range(c):
#     for j in range(r):
#         print(l[j][i],end=" ")
#     print()


# r=int(input())
# c=int(input())
# l=[]
# d=0
# for i in range(r):
#     k=list(map(int,input().split()))
#     l.append(k)
# for i in range(r):
#     for j in range(c):
#         if i==j and l[i][j]==1:
#             d=d+1
#         elif i!=j and l[i][j]==0:
#             d=d+1
#     print()
# if d==r*c:
#     print("identity")
# else:
#     print("not")


# r=int(input())
# c=int(input())
# l=[]
# for i in range(r):
#     k=list(map(int,input().split()))
#     l.append(k)
# sum=0
# for i in range(r):
#     for j in range(c):
#         sum=sum+l[i][j]
# print(sum)

# 1
# r=int(input())
# c=int(input())
# l=[]
# for i in range(r):
#     k=list(map(int,input().split()))
#     l.append(k)
# print(l)
# for i in range(r):
#     for j in range(c):
#         print(l[i][j],end=" ")
#     print()


# 2
# r=int(input())
# c=int(input())
# l=[]
# for i in range(r):
#     k=list(map(int,input().split()))
#     l.append(k)
# n=int(input())
# a=0
# for i in range(r):
#     for j in range(c):
#         if l[i][j]==n:
#             print(i,j)
#             a=1


# 3
# r=int(input())
# c=int(input())
# l=[]
# for i in range(r):
#     k=list(map(int,input().split()))
#     l.append(k)
# h1=l[0][0]
# h2=l[0][0]
# for i in range(r):
#     for j in range(c):
#         if l[i][j]>h1:
#             h2=h1
#             h1=l[i][j]
#         elif l[i][j]>h2 and l[i][j]!=h1:
#             h2=l[i][j]
# print(h2)


# 4
# r=int(input())
# c=int(input())
# l=[]
# for i in range(r):
#     k=list(map(int,input().split()))
#     l.append(k)
# sum=0
# for i in range(r):
#     for j in range(c):
#         sum=sum+l[i][j]
# print(sum)


# 5
# r=int(input())
# c=int(input())
# l=[]
# for i in range(r):
#     k = list(map(int, input().split()))
#     l.append(k)
# sum=0
# c1=0
# for i in range(r):
#     for j in range(c):
#         if l[i][j]%2==1:
#             sum=sum+l[i][j]
#             c1=c1+1
# if c1!=0:
#     print(sum//c1)


# 6
# n=int(input())
# l=[]
# for i in range(n):
#     k=list(map(int,input().split()))
#     l.append(k)
# h=l[0][0]
# for i in range(n):
#     if l[i][i]>h:
#         h=l[i][i]
#     if l[i][n-1-i]>h:
#         h=l[i][n-1-i]
# for i in range(n):
#     l[i][i]=h
#     l[i][n-1-i]=h
# for i in range(n):
#     print(*l[i])


# 7
# r=int(input())
# c=int(input())
# l=[]
# for i in range(r):
#     k=list(map(int,input().split()))
#     l.append(k)
# sum1=0
# sum2=0
# for i in range(r):
#     sum1=sum1+l[i][i]
#     sum2=sum2+l[i][r-i-1]
# print(sum1)
# print(sum2)


# 8
# r=int(input())
# c=int(input())
# l=[]
# for i in range(r):
#     k=list(map(int,input().split()))
#     l.append(k)
# for i in range(r-1,-1,-1):
#     print(*l[i])


# 9
# r=int(input())
# c=int(input())
# l=[]
# d=0
# for i in range(r):
#     k=list(map(int,input().split()))
#     l.append(k)
# for i in range(r):
#     for j in range(c):
#         if i==j and l[i][j]==1:
#             d=d+1
#         elif i!=j and l[i][j]==0:
#             d=d+1
# if d==r*c:
#     print("yes")
# else:
#     print("no")


# 9
# r=int(input())
# c=int(input())
# l=[]
# for i in range(r):
#     k=list(map(int,input().split()))
#     l.append(k)
# a=1
# for i in range(r):
#     for j in range(c):
#         if i==j:
#             if l[i][j]!=7:
#                 a=0
#         else:
#             if l[i][j]!=0:
#                 a=0
# if a==1:
#     print("7 identity")
# else:
#     print("no")


# 10
# r=int(input())
# c=int(input())
# l=[]
# for i in range(r):
#     k=list(map(int,input().split()))
#     l.append(k)
# a=1
# b=1
# for i in range(r):
#     for j in range(1,c):
#         if l[i][j]!=l[i][0]:
#             a=0
# for i in range(c):
#     for j in range(1,r):
#         if l[i][j]!=l[0][j]:
#             b=0
# if a==1:
#     print("equal row")
# elif b==1:
#     print("equal column")
# else:
#     print("no")


# 11
# r=int(input())
# c=int(input())
# l=[]
# for i in range(r):
#     k=list(map(int,input().split()))
#     l.append(k)
# a=[]
# for i in range(r):
#     for j in range(c):
#         a.append(l[i][j])
# a.sort()
# k=0
# for i in range(r):
#     for j in range(c):
#         l[i][j]=a[k]
#         k=k+1
# for i in range(r):
#     print(*l[i])


# n=int(input())
# digits=[]
# for i in str(n):
#     digits.append(int(i))
# c=len(digits)
# while(True):
#     total=0
#     for i in digits[-c:]:
#         total=total+i
#     digits.append(total)
#     if total==n:
#         print("yes")
#         break
#     if total>n:
#         print("no")
#         break
#
#
# n=int(input())
# digits=[]
# for i in str(n):
#     digits.append(int(i))
# c=len(digits)
# while(True):
#     total=0
#     for i in digits[-c:]:
#         total=total+i
#     digits.append(total)
#     if total==n:
#         print("yes")
#         break
#     if total>n:
#         print("no")
#         break


# n=int(input())
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c=c+1
# if c!=2:
#     print(n)
# else:
#     t=n
#     p=1
#     while(t>0):
#         r=t%10
#         p=p*r
#         t=t//10
#     result=n+p
#     next_prime=n+1
#     while True:
#         c=0
#         for i in range(1,next_prime+1):
#             if next_prime%i==0:
#                 c=c+1
#         if c==2:
#             break
#         next_prime+=1
#     if result==next_prime:
#         print(n,"pointer")
#     else:
#         print(n,"not")


# n=int(input())
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c=c+1
# if c!=2:
#     print(n)
# else:
#     t=n
#     p=1
#     while(t>0):
#         r=t%10
#         p=p+r
#         t=t//10
#     result=n+p
#     next_prime=n+1
#     while(True):
#         c=0
#         for i in range(1,next_prime+1):
#             if next_prime%i==0:
#                 c=c+1
#         if c==2:
#             break
#         next_prime+=1
#     if result==next_prime:
#         print(n,"pointer")
#     else:
#         print(n,"not pointer")

# def prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc=fc+1
#     if fc==2:
#         return True
#     else:
#         return False
# n=int(input())
# sum=0
# while(n>0):
#     r=n%10
#     n=n//10
#     if prime(r):
#         sum=sum+r
# if sum==0:
#     print("no")
# else:
#     print(sum)


# n=int(input())
# t=n
# sum=0
# while(n!=0):
#     r=n%10
#     fact=1
#     for i in range(1,r+1):
#         fact=fact*i
#     sum=sum+fact
#     n=n//10
# if t==sum:
#     print("strong")
# else:
#     print("not")


# n=int(input())
# i=1
# while(True):
#     a=i*(i+1)
#     if a==n:
#         print("pronic")
#         break
#     if a>n:
#         print("not")
#         break
#     i=i+1

# n=int(input())
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print("perfect")
# else:
#     print("not")

# n=int(input())
# a=n**2
# sum=0
# while(a>0):
#     r=a%10
#     sum=sum+r
#     a=a//10
# if n==sum:
#     print("neon")


# n=int(input())
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c=c+1
# if c!=2:
#     print(n)
# else:
#     t=n
#     p=1
#     while(t>0):
#         r=t%10
#         p=p*r
#         t=t//10
#     result=n+p
#     next_prime=n+1
#     while(True):
#         c=0
#         for i in range(1,next_prime+1):
#             if next_prime%i==0:
#                 c=c+1
#         if c==2:
#             break
#         next_prime+=1
#     if result==next_prime:
#         print(n,"pointer")
#     else:
#         print(n,"not")


# n=int(input())
# digits=[]
# for i in str(n):
#     digits.append(int(i))
# c=len(digits)
# while(True):
#     total=0
#     for i in digits[-c:]:
#         total=total+i
#     digits.append(total)
#     if total==n:
#         print("k")
#     if total>n:
#         print("not")

# n=int(input())
# sum=0
# while(n>0):
#     r=n%10
#     if r==2 or r==3 or r==5 or r==7:
#         sum=sum+r
#     n=n//10
# print(sum)

# n=int(input())
# a,b=0,1
# for i in range(n):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c


l=list(map(int,input().split()))
a=0
for i in l:
    a=a*10+i
a=a+1
l=[]
while a>0:
    r=a%10
    l.insert(0,r)
    a=a//10
print(l)




















