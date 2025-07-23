# selection sort

#step1=find the min value
#step2 swap the position  the length of array
#position start from index 1

arr=[4,2,3,1,6,5]
for pos in range(len(arr)):
    min=pos
    for i in range(pos+1,len(arr)):
        if arr[i]<arr[min]:
            min=i
    arr[min],arr[pos]=arr[pos],arr[min]
print(arr)

