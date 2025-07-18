# count vowels and consonant


s="mohamed nabil"
vowel="aeiouAEIOU"
count_vowels=0
count_consonant=0

for ch in  s:
    if ch.isalpha():
        if ch in vowel:
            count_vowels+=1
        else:
             count_consonant+=1

print("the count of vowels:",count_vowels)
print("the count of consonats",count_consonant)
