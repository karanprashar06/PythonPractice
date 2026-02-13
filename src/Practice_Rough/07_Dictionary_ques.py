

varibale = "good morning"
#good morning
dict ={}

for i in varibale:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)
print(type(dict))