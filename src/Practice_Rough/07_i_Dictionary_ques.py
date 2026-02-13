# Frequency of Characters in a String
# Write a program to count the frequency
# of each character in a given string.


string = "automation"

string1 = input("\n Enter the input string : ")

dict ={}
for i in string:
    dict[i] = dict.get(i, 0) + 1

print(dict)