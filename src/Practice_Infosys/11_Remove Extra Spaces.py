def remove_extra_spaces(sentence):
    words = sentence.split()
    return " ".join(words)

print(remove_extra_spaces("  Python   is   great  "))