def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}

    for char in s1:
        count[char] = count.get(char, 0) + 1

    for char in s2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True

s1 = input("Enter first string: ").lower().replace(" ", "")
s2 = input("Enter second string: ").lower().replace(" ", "")

print("Anagram" if is_anagram(s1, s2) else "Not an anagram")
