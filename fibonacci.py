# fibonacci series upto  n terms

n=int(input("The enter a number:"))
a,b=0,1
c=0
print("Fibonnaci series up to ",n,"terms:")
while c<n:
    print(a,end="")
    a,b=b,a+b
    c+=1
