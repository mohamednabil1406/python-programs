l = [1, 2, 3, 2, 1]
is_palindrome = True

i = 0
while i < len(l) // 2:
    if l[i] != l[len(l) - 1 - i]:
        is_palindrome = False
        break
    i += 1

if is_palindrome:
    print("List is a palindrome")
else:
    print("List is not a palindrome")
