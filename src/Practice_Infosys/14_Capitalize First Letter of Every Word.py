
str1 = "My name is karan"
def capitalize_first_letter(str):
    n= str1.split()
    print(n)
    result = [ word.capitalize() for word in n]
    print(result)
    print(" ".join(result))
capitalize_first_letter(str1)


