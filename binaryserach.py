arr = [1, 3, 5, 7, 9, 11, 13]
t = 9
l = 0
r = len(arr) - 1
found = False  # Initialize before loop

while l <= r:
    mid = (l + r) // 2
    if arr[mid] == t:
        print("Found the target at index", mid)
        found = True
        break  # Optional: stop after finding
    elif arr[mid] < t:
        l = mid + 1
    else:
        r = mid - 1

if not found:
    print("The target is not found")
