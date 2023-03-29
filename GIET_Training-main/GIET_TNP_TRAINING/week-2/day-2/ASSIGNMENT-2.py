'''
given two lists, both having integer elements, write a python program using python lists to create and
return a new list as per the rule given below: If the double of an element in list1 is present in list2, then add it to the new list.

Estimated Time: 20 minutes

Sample Input

list1 [11,8,23,7,25,15] - list2 [6,33,50,31,46,78,16,34] -

Expected Output

new_list [8,23,25]
'''
l1=list(map(int,input().split(",")))
l2=list(map(int,input().split(",")))
res=[]
for i in l1:
    if i*2 in l2:
        res.append(i)
print(res)