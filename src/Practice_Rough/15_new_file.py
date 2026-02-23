input_string = input("Enter a string: ")
#My name is karan
#na raks ie manyM


words = input_string.split()
lengths = [len(word) for word in words]

print(lengths)

rev = input_string[::-1].replace(" ", "")
print(rev)

result=[]
index= 0
for i in lengths:
    result.append(rev[index: index + i])
    index+=i

print("output_string =", " ".join(result))
