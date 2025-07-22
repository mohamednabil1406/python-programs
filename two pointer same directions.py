# two  pointers same directions

#using duplicates in array
def remove_duplicates(arr):
    if not arr:
        return 0
    s = 0
    for f in range(1, len(arr)):
        if arr[s] != arr[f]:
            s += 1
            arr[s] = arr[f]
    return s + 1  # Length of unique part

arr = [1, 2, 3, 3, 4, 5, 6, 6]
length = remove_duplicates(arr)
print("The array after removing duplicates:", arr[:length])
print("Length of unique elements:", length)
