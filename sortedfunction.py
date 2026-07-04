#4..l=[('meghana',21),('roshini',19),('sravan',30),('pravallika',26)]
#k=sorted(l,key=lambda x:x[1],reverse=True)
#print(k)

from functools import reduce
l=[5,10,15,20,25,30]
k=reduce(lambda x,y:x+y,filter(lambda x:x%5==0,map(lambda x:x**2,l)))
print(k)