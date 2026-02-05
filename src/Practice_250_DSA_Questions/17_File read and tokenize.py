# Reading a File (Concept + Code)
#
# Concept:
# Reading a file means opening a file stored on the system and loading its contents into the program so it can be processed.
#
# Code example
# with open("sample.txt", "r") as file:
#     content = file.read()
#
# What happens here:
#
# open("sample.txt", "r") → opens the file in read mode
#
# file.read() → reads the entire file as one string
#
# content → stores the file text in memory
#
# 🔤 Tokenization (Concept + Code)
#
# Concept:
# Tokenization means breaking text into smaller pieces (tokens), usually words, so the program can analyze or process them.
#
# Code example
# tokens = content.split()
#
# What happens here:
#
# split() → divides the string into words using spaces
#
# Each word becomes a token
#
# 🔗 Combined: File Reading + Tokenization
# with open("sample.txt", "r") as file:
#     content = file.read()
#
# tokens = content.split()
# print(tokens)
#
# Example file (sample.txt)
# Python is easy to learn
#
# Output
# ['Python', 'is', 'easy', 'to', 'learn']
#
# 🧠 Simple Explanation
#
# File reading → get text from a file
#
# Tokenization → break text into words
#
# Together → convert file content into usable data