def moves_zeroes(arr):
    s = 0
    for f in range(len(arr)):
        if arr[f] != 0:
            arr[s], arr[f] = arr[f], arr[s]
            s += 1
    return arr

arr = [0, 1, 0, 2, 3, 5]
print(moves_zeroes(arr))  # prints: [1, 2, 3, 5, 0, 0]
#ou