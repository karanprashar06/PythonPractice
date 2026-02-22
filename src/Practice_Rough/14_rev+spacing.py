input_string =input("Enter a string:")
words=input_string.split()
lengths = [len(word) for  word in words]
print(lengths)


rev = input_string[::-1].replace(" ", "")
print(rev)
result = []
index = 0

for length in lengths:
        result.append(rev[index: index + length])
        index+=length
print("output_string =", " ".join(result))
