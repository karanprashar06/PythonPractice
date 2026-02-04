n = int(input("Enter the number: "))
rev =int(str(n)[::-1])
# if n == rev:
#     print("The number Palindrome",sep="++")
# else:
#     print("Not Palindrome", sep="++")

print("Palindrome" if n == rev else "Not Palindrome")