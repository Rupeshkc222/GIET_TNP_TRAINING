'''
Given two lists both having String elements, write a python program using python list to create new string as per the following rule given below
First Element in list1 should be merged with last element of list2
Second Element in list2 should be merged with secondlast element of list2

If an element is in list1/list2 is None then corresponding element in the other list should be kept as it is in the merge list

> list1=['A','app','a','d','ke','th','doc','awa']

> list2=['y','tor','e','eps','ay',None,'le,'n']

Expected output:
"An apple a day keeps the docter away"
'''

list1=['A','app','a','d','ke','th','doc','awa']
list2=['y','tor','e','eps','ay',None,'le','n']
n_2=list2[::-1]
res=""
for i in range(len(list1)):
    if n_2[i]==None:
        res=res+list1[i]+" "
    else:
        res=res+list1[i]+n_2[i]+" "
print(res)
