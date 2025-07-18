# second largest element in list
l=[12,34,35,67]
f=s=-999999
i=0
while i<len(l):
    if l[i]>f:
        s=f
        f=l[i]
    elif l[i] > s and l[i]!=f:
        s=l[i]
    i+=1
print("the second largest value :",s)


# output : 35