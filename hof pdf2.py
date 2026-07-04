#2..a=[1,2,3,4]
#b=[10,20,30,40]
#k=list(map(lambda x,y:x+y,a,b))
#print(k)

#3..nums=[12,15,7,18,20,21,25]
#k=list(filter(lambda x: x%3==0 or x%5==0,nums))
#print(k)

#4..from functools import reduce
#nums=[1,2,3,4]
#k=reduce(lambda x,y:x+y,nums,10)
#print(k)

nums=[[1,2],[3,4],[5,6]]
#result=list(map(lambda x:x.append(10),nums))
# #//it returns none because it stores the value but not returns so the output becomes none. so, for this we need modify as x+[10] then it append to the list and give the correct output
result=list(map(lambda x:x+[10],nums))
print("result:", result)
print("nums:", nums)