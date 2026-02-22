string = "good morning"

dict={}

for char in string:
    if char in dict:
        dict[char]=dict.get(char,0)+1
    else:
        dict[char]=1
print(dict.items())