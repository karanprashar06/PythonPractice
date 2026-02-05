n = input("Enter a string: ")

rev = n[::-1]

print(f"The string {n} Palindrome" if n == rev else f"The string {n} Not Palindrome")