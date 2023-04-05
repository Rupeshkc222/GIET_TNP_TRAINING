#linear search

def linearSearch(arr,n,x):
    for i in range(0,n):
        if arr[i] == x:
            return i
    return -1
arr=[2,9,5,0,6,4]
to_f=int(input("enter the number to find in list"))
r=linearSearch(arr,len(arr),to_f)
if r ==-1:
    print("not found")
else:
    print("element found in index position",r)