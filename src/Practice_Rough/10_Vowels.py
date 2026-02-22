input_string ="Goodbye"

vowels ="aeiou"

vowel_count = 0
result=[]

for i in input_string:
    if i in vowels:
        vowel_count += 1
        result.append(i)

print(vowel_count)
print(result)