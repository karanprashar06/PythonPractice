

str1= "karan karan is boy boy"

new = str1.split()
print(new)
new1 = set(new)
print(new1)

print(" ".join(new1))


def remove_duplicate_words(sentence):
    words = sentence.split()
    seen = set()
    result = []

    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)

    return " ".join(result)


print(remove_duplicate_words("python is is easy easy"))
