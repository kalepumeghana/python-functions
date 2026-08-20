# ITERATOR IS AN OBJECT THAT LET'S YOU GO THROUGH AN ELEMENT IN AN ORDER ONE BY ONE ANS ALSO REMEMBERS ITS CURRENT STATE.

# l=["hello",1,2,(3,4)]
# p=iter(l)
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# # print(next(p)) // it gives an error because it is out of range
#
#
# s="abc"
# k=iter(s)
# l=iter(s)
# print(next(k))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(k))
# print(next(k))
#
#
# s={1,2,3,4,5}
# a=iter(s)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# # print(next(a))   error out of an range
#
#
#
# d={'a':10,'b':20,'c':30}
# a=iter(d)
# print(next(a))
# print(next(a))
# print(next(a))
#
#
# t=(5,6,7)
# t1=iter(t)
# t2=t. __iter__()
# print(next(t1))
# print(t1.__next__())
# print(t1.__next__())
# print(next(t2))
# print(next(t2))
# print(next(t2))


# class list_iter:
#     def __init__(self,l):
#         self.l=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<len(self.l):
#             i=self.index
#             self.index+=1
#             return self.l[i]
#         else:
#             raise StopIteration
# a=list_iter([1,2,3,4,5,9,0])
# for i in a:
#     print(i)
#
#
# class Even:
#     def __init__(self,l):
#         self.l=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index<len(self.l):
#             i=self.index
#             self.index+=1
#             if self.l[i]%2==0:
#                 return self.l[i]
#         raise StopIteration
# a=Even([1,2,3,4,5,9,0])
# for i in a:
#     print(i)


# CREATE A CUSTOM ITERATOR THAT RETURNS VOWELS FROM THE GIVEN STRING
# class Vowels:
#     def __init__(self,l):
#         self.l=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index<len(self.l):
#             index=self.index
#             self.index+=1
#             if self.l[index] in "aeiou":
#                 return self.l[index]
#         raise StopIteration
#
# v1=Vowels("Just thinking")
# it=iter(v1)
# print(next(it))

# Create a custom iterator that takes list of numbers and retake the current highest
# class Highest:
#     def __init__(self,l):
#         self.l=l
#         self.index=0
#         self.high=l[0]
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<len(self.l):
#             i=self.index
#             self.index+=1
#             if self.l[i]>self.high:
#                 self.high=self.l[i]
#             return self.high
#         raise StopIteration
# l=Highest([7,5,3,8,6,9,2,10])
# for i in l:
#     print(i)


# fruits=['apple','banana','orange']
# a=iter(fruits)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# a=iter([1,2])
# print(next(a))
# print(next(a))
# print(next(a,'d'))

# class Count:
#     def __init__(self,start,stop):
#         self.start=start
#         self.stop=stop
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start>self.stop:
#             raise StopIteration
#         a=self.start
#         self.start+=1
#         return a
# c=Count(1,5)
# for i in c:
#     print(i)


# 1
# class Num:
#     def __init__(self,n):
#         self.n=n
#         self.a=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.a<=self.n:
#             a=self.a
#             self.a+=1
#             return a
#         raise StopIteration
# N=Num(20)
# for i in N:
#     print(i)


# 2
# class Even:
#     def __init__(self,n):
#         self.n=n
#         self.i=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.i<len(self.n):
#             b=self.i
#             self.i+=1
#             if self.n[b]%2==0:
#                 return self.n[b]
#         raise StopIteration
# a=Even([2,8,5,66,77,44,100])
# for i in a:
#     print(i)


# 3
# class Reverse:
#     def __init__(self,text):
#         self.text=text
#         self.index=len(text)-1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index>=0:
#             ch=self.text[self.index]
#             self.index-=1
#             return ch
#         raise StopIteration
# r=Reverse("meghana")
# for ch in r:
#     print(ch)


# 4
# class Index:
#     def __init__(self,n):
#         self.n=n
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<len(self.n):
#             a=(self.index,self.n[self.index])
#             self.index+=1
#             return a
#         raise StopIteration
# l=[1,2,3,4,5]
# a=Index(l)
# for i in a:
#     print(i)


class Words:
    def __init__(self,n):
        self.n=n.split(
            
        )
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<len(self.n):
            a=self.n[self.index]
            self.index+=1
            return a
        raise StopIteration
l="i am meghana"
w=Words(l)
for i in w:
    print(i)


# 9
# class Indices:
#     def __init__(self,text):
#         self.text=text
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<len(self.text):
#             ch=self.text[self.index]
#             self.index+=2
#             return ch
#         raise StopIteration
# i=Indices("meghana")
# for ch in i:
#     print(ch)


# 1
# class Numbers:
#     def __init__(self,n):
#         self.n=n
#         self.index=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<=self.n:
#             a=self.index
#             self.index+=1
#             return a
#         raise StopIteration
# n=Numbers(15)
# for a in n:
#     print(a)


# 2
# class Num:
#     def __init__(self,n):
#         self.n=n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n>=1:
#             a=self.n
#             self.n-=1
#             return a
#         raise StopIteration
# n=Num(10)
# for a in n:
#     print(a)

# 3
# class Even:
#     def __init__(self,n):
#         self.n=n
#         self.index=0
#         self.num=2
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index < self.n:
#             b=self.num
#             self.num+=2
#             self.index+=1
#             return b
#         raise StopIteration
# e=Even(10)
# for b in e:
#     print(b)


# 4
# class Odd:
#     def __init__(self,n):
#         self.n=n
#         self.index=0
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<self.n:
#             a=self.num
#             self.num+=2
#             self.index+=1
#             return a
#         raise StopIteration
# o=Odd(5)
# for a in o:
#     print(a)


# 5
# class Even:
#     def __init__(self,n):
#         self.n=n
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index<len(self.n):
#             a=self.index
#             self.index+=1
#             if self.n[a]%2==0:
#                 return self.n[a]
#         raise StopIteration
# e=Even([1,4,7,88,44,66,77,33,89])
# for a in e:
#     print(a)


# 6
# class Odd:
#     def __init__(self,n):
#         self.n=n
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index<len(self.n):
#             a=self.index
#             self.index+=1
#             if self.n[a]%2==1:
#                 return self.n[a]
#         raise StopIteration
# o=Odd([1,5,9,55,88,33])
# for a in o:
#     print(a)


# 7
# class Positive:
#     def __init__(self,n):
#         self.n=n
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index<len(self.n):
#             a=self.n[self.index]
#             self.index+=1
#             if a>0:
#                 return a
#         raise StopIteration
# p=Positive([1,-5,7,-4])
# for a in p:
#     print(a)


# 8
# class Char:
#     def __init__(self,n):
#         self.n=n
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<len(self.n):
#             ch=self.n[self.index]
#             self.index+=1
#             return ch
#         raise StopIteration
# c=Char("hello")
# for ch in c:
#     print(ch)


# 9
# class Reverse:
#     def __init__(self,n):
#         self.n=n
#         self.index=len(n)-1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index>=0:
#             r=self.n[self.index]
#             self.index-=1
#             return r
#         raise StopIteration
# a=Reverse("hii")
# for r in a:
#     print(r)
