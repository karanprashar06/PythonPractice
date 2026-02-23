def sort_by_length(sentence):
    words = sentence.split()
    words.sort(key=len)
    return " ".join(words)

print(sort_by_length("Python is a powerful language"))