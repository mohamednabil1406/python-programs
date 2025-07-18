# armstrong number

num=int(input("Enter  a number "))
t=num
o=0
n=num
while n!=0:
    n//=10
    o+=1

s=0
n=num
while n!=0:
    d=n%10
    p=1
    for _  in range(o):
        p*=d
    s+=p
    n//=10
if s==num:
    print(num,"is an  armstrong number ")
else:
    print(num,"is not an a armstrong number")