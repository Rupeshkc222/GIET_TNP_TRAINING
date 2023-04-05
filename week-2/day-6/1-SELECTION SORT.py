def SelectionSort(arr,size):
    for step in range(size):
        min_idx=step
        for i in range(step+1,size):
            if arr[i]<arr[min_idx]:
                min_idx=i
        (arr[step],arr[min_idx])=(arr[min_idx],arr[step])
    return arr
data=[20,12,10,15,2]
size=len(data)
print(SelectionSort(data,size))