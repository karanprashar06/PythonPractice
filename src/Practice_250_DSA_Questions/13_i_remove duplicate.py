def removing_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return " ".join(result)
ok = removing_duplicates("KARAN")
print(ok)