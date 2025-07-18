#buuble sort array


arr = [64, 34, 25, 12, 22, 11, 90]
n=len(arr)-1
i=0
while i<n:
    j=0
    while j<n-i-1:
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
        j+=1
    i+=1
print("the bubble sort of arr:",arr)