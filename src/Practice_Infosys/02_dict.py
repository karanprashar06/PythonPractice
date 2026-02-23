input_steing = input("Enter a string: ")

result = {}

for char in input_steing:
    result[char] = result.get(char, 0) + 1

print(result)
print(result.items())