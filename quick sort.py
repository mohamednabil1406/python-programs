# quick sort array

# choice the random pivot element
#store the left []
#store the right[]
# merge the left + middle+right



import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    left = [i for i in arr if i < pivot]
    mid = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]

    return quicksort(left) + mid + quicksort(right)

arr = [2, 3, 6, 4, 8, 7, 1]
print("Before sorting:", arr)
sorted_arr = quicksort(arr)
print("After sorting: ", sorted_arr)
