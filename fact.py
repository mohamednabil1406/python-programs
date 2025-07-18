# factorial num

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print("the factorial number of 5 is :",fact(5))