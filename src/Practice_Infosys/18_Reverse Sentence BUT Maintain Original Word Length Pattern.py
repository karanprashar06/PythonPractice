def special_reverse(sentence):
    words = sentence.split()
    lengths = [len(word) for word in words]

    rev = sentence[::-1].replace(" ", "")

    result = []
    index = 0

    for length in lengths:
        result.append(rev[index:index + length])
        index += length

    return " ".join(result)


print(special_reverse("My name captain"))