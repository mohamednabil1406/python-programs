# insertion sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > k:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k

arr = [5, 2, 9, 1, 5, 6]
insertion_sort(arr)
print("Insertion Sorted:", arr)

# output
#Insertion Sorted: [1, 2, 5, 5, 6, 9]
