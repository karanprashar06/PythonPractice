s = input('enter a string: ')

def find_duplicates(s):
    seen = set()
    duplicates = set()

    for char in s:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)

    return " ".join(duplicates)

result = find_duplicates(s)

if result:
    print(f"Duplicate characters are -- {result}")
else:
    print("No duplicate characters found")
