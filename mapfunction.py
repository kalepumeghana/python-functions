#1..a=[2,5.6,8,9]
#l=list(map(lambda x:x*(9/5)+32,a))
#print(l)

#        (or)
#1..a=[2.6,8,9]
#def cel(f):
#    return f*(9/5)+32
#l=list(map(cel,a))
#print(l)


#5..a=[1,2,3,4,5,6,7,8,9,10]
#l=list(map(lambda x:x*2,filter(lambda x:x%3==0,a)))
#print(l)


#1..l=[[1,2],[3,4],[5,6]]
#k=list(map(lambda x:x+[5],l))
#print(k)
#when we write lambda x:x.append(5) it gives none because it only stores the value but not return


#5..l="hello i am meghana"
#k=list(map(ord,l))
#print(k)


#8..l=[10,350,10,350,20]
#k=list(map(id,l))
#print(k)
