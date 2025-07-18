l = [1, 2, 3, 4, 5, 5, 6, 7, 7]
unique = []

for i in range(len(l)):
    duplicate = False
    for j in range(len(unique)):
        if l[i] == unique[j]:
            duplicate = True
            break
    if not duplicate:
        unique.append(l[i])

print("After removing duplicates:", unique)
