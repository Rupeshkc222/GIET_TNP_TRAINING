#binary_search
def binary_Search(arr,x,low,high):
    while(low<high):
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid
    return -1
arr=[2,3,4,5,6,7,9]
to_f=int(input("to find"))
r=binary_Search(arr,to_f,0,len(arr)-1)
if r==-1:
    print("not found")
else:
    print("element is found at",r)
