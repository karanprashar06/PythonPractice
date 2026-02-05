n = input("Enter the sentence you want to reverse: ")

# def reverseSentence(sentence):
#     return " ".join(sentence.split()[::-1])
# ok = reverseSentence(n)
# print(f"The reverse sentence is-- {ok} ")

#
# def reverseSentence(sentence):
#     return "".join(sentence[::-1])
# ok = reverseSentence(n)
# print(f"The reverse sentence is-- {ok} ")

def reverseSentence(sentence):
    return " ".join(sentence.split())
ok = reverseSentence(n)
print(f"The reverse sentence is-- {ok} ")
