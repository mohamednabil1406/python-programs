# reverse the numbers

n=12345
r=0

while n!=0:
    digit=n%10
    r=(r*10)+digit
    n//=10
print("the reverse number is  :",r)