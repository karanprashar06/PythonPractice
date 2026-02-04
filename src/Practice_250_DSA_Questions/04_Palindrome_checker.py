def Palindrome(num):
    rev = str(num)[::-1]
    print("Palindrome" if num == rev else "Not a Palindrome")

Palindrome("AKA")
Palindrome("ALKSKLA")
Palindrome("AKSHAY")