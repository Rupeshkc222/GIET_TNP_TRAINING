#Paired Output
list1=[9,3,6,1,5,0,8,2,4,7]
list2=[6,4,6,1,2]
#result=[(6,2),(4,8),(6,2),(1,3),(2,7)]
result = [(num, list1.index(num)) for num in list2 if num in list1]
print(result)


#using for loop
mylist=[9,3,6,1,5,0,2,4,7]
list_b=[6,4,1,2,2]
res=[]
for i in list_b:
    if i in mylist:
        res.append((i,mylist.index(i)))
    else:
        res.append((i,"not found"))
print(res)
    
