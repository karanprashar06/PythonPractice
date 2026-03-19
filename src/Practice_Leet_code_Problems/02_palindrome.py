

def check_palindrome(num):
    s=  str(num)

    return s == s[::-1]

print(check_palindrome(121))
print(check_palindrome("iifii"))
print(check_palindrome(123213))
print(check_palindrome(1001))