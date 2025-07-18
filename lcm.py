x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

a, b = x, y

# GCD using Euclidean algorithm
while b != 0:
    a, b = b, a % b

gcd = a
lcm = (x * y) // gcd

print("The LCM of the numbers is:", lcm)
