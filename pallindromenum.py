# pallindrome number check

n=212
o=n
r=0
while n!=0:
    digit=n%10
    r=(r*10)+digit
    n//=10
if r==o:
    print("the numbers is pallindrome ",o)
else:
    print("not a pallindrome")