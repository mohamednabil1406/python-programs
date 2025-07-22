# example of two pointers

arr=[1,2,3,4,5,6]
t=10
h=1# flag
l=0 # postion from o index left
r=len(arr)-1 # position  of r pointer index
while l < r:
    new=arr[l]+arr[r]
    if new==t:
        h=0
        print(l,r)
        break
    elif new<t:
        l+=1
    elif new>t:
        r-=1
if h==1:
    print("no  target found")