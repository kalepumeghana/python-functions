#l=["Hello","hii","Bye"]
#k=list(filter(lambda x:x[0].isupper(),l))
#print(k)

#from functools import reduce
#l=[1,2,3,4,5]
#k=reduce(lambda x,y:x*y,l)
#print(k)

#l=[('meghana',21),('sravan',30),('roshini',19),('pravallika',26)]
# k=list(sorted(l,key=lambda x:x[1],reverse=True))
# print(k)

# l=[1,2,3,4,5,6,7,8,9,10]
# k=list(filter(lambda x:x%2!=0,map(lambda x:x**2,l)))
# print(k)


# from functools import reduce
# l=['cat','elephant','dog','rhinoceros']
# k=reduce(lambda x,y:x if len(x)>len(y) else y,l)
# print(k)

# def add(x,y):
#     def display(x,y):
#         print(x,y)
# add(10,20)

def fun():
    x=700
    def fun2():
        nonlocal x
        def fun3():
            nonlocal x
            print(x)
        fun3()
    print(x)
    fun2()
    print(x)
fun()