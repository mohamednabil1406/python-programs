def missingarray(arr):
    n = len(arr)
    total = n * (n + 1) // 2   # Expected sum from 0 to n
    actual = sum(arr)          # Actual sum of given array
    return total - actual      # Missing number

arr = [0, 1, 2, 4]  # Missing number is 3
print("The missing element in the array is:", missingarray(arr))
