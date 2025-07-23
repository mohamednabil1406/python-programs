  # bubble sort
arr=[1,10,5,2,11]
for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1):
        if arr[j]<arr[j+1]:
            continue
        elif arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("the sorted array is",arr)


