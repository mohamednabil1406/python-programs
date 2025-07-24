def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Step 1: Recursively sort the halves
        mergesort(left)
        mergesort(right)

        # Step 2: Merge using two pointers
        lp = 0  # left pointer
        rp = 0  # right pointer
        fp = 0  # final pointer (for merged array)

        # Compare and merge
        while lp < len(left) and rp < len(right):
            if left[lp] < right[rp]:
                arr[fp] = left[lp]
                lp += 1
            else:
                arr[fp] = right[rp]
                rp += 1
            fp += 1

        # Copy remaining elements (if any)
        while lp < len(left):
            arr[fp] = left[lp]
            lp += 1
            fp += 1

        while rp < len(right):
            arr[fp] = right[rp]
            rp += 1
            fp += 1


arr = [4, 5, 3, 1, 2, 6, 7]
print("Before:", arr)
mergesort(arr)
print("After: ", arr)
