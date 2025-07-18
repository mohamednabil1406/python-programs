s = "aaabbccdefghii"
f = []
i = 0
while i < len(s):
    ch = s[i]
    found = False

    j = 0
    while j < len(f):
        if f[j][0] == ch:
            f[j][1] += 1
            found = True
            break
        j += 1

    if not found:
        f.append([ch, 1])

    i += 1

# Display frequencies
k = 0
while k < len(f):
    print(f[k][0], ":", f[k][1])
    k += 1
