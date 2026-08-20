# GENERATOR IS A SPECIAL TYPE OF FUNCTION THAT GENERATES VALUES WHEN IT IS CALLED USING YIELD KEYWORD
# def fun(x):
#     for i in range(x):
#         yield i
# g=fun(25)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def fun(x):
#     yield x
#     yield x+1
#     yield x+4
#     yield x+10
# a=fun(10)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


# def even(x):
#     for i in range(x):
#         if i%2==0:
#             yield i
# e=even(10)
# print(next(e))
# print(next(e))
# print(next(e))
# print(next(e))
# print(next(e))
# print(next(e)) //stop iteration


# def odd(x):
#     for i in range(x):
#         if i%2!=0:
#             yield i
# o=odd(10)
# print(next(o))
# print(next(o))
# print(next(o))
# print(next(o))
# print(next(o))


# def alter(*args):
#     c=0
#     for i in args:
#         c=c+1
#         if c%2==1:
#             yield i
# a=alter(1,4,5,6,7)
# print(next(a))
# print(next(a))
# print(next(a))


# def char(x):
#     for i in x:
#         yield i
# c=char("meghana")
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c)) //stop iteration


# def prime(x):
#     for i in range(2,x+1):
#         fc=0
#         for j in range(1,i+1):
#             if(i%j==0):
#                 fc=fc+1
#         if(fc==2):
#             yield i
# p=prime(10)
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# # print(next(p)) //stop iteration


# 1
# def num(x):
#     for i in range(1,x+1):
#         yield i
# n=num(10)
# for i in n:
#     print(i)
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# # print(next(n))
# # print(next(n))


# 2
# def even(x):
#     for i in range(1,x+1):
#         if i%2==0:
#             yield i
# e=even(10)
# for i in e:
#     print(i)
# print(next(e))


# 3
# def char(x):
#     for i in (x):
#         yield i
# c=char("meghana")
# for i in c:
#     print(i)


# 4
# def char(x):
#     a=len(x)-1
#     for i in range(a,-1,-1):
#         yield x[i]
# c=char("meghana")
# for i in c:
#     print(i)


# 5
# def vowels(x):
#     a=len(x)
#     for i in range(0,a):
#         if x[i] in "aeiou":
#             yield x[i]
# v=vowels("meghana")
# for i in v:
#     print(i)\


# 6
# def digit(x):
#     a=len(x)
#     for i in range(0,a):
#         if x[i].isdigit():
#             yield x[i]
# d=digit("m4nj34")
# for i in d:
#     print(i)


# 7
# def square(x):
#     for i in x:
#         yield i*i
# s=square([1,2,3,4,5])
# for i in s:
#     print(i)


# 8
# def digit(x):
#     for i in str(x):
#         yield int(i)
# a=digit(122333)
# for i in a:
#     print(i)


# 9
def cumulative(x):
    total=0
    for i in (x):
        total=total+i
        yield total
a=cumulative([1,2,3])
for i in a:
    print(i)

















