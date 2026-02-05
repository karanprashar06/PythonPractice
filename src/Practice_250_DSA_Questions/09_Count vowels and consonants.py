name=input("Enter your name: ")

def countvowels(s):
    vowels = []
    consonants = []
    for char in s.lower():
        if char.isalpha():
            if char in "aeiou":
                vowels.append(char)
            else:
                consonants.append(char)
        else:
            print("Invalid character")
            #break
    total_vowels = len(vowels)
    total_consonants = len(consonants)
    print(f"constant are {total_consonants} and vowels are {total_vowels}")

countvowels(name)