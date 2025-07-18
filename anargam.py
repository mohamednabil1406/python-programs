def isAnagram(s, t):
    if len(s) != len(t):
        return False
    count = [0] * 26  # assuming only 'a' to 'z'
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    for c in count:
        if c != 0:
            return False

    return True
print(isAnagram("listen","silent"))
print(isAnagram("race","care"))