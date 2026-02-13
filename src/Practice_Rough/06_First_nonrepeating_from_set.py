# find out the first non-repeating from the string

s = set()

def first_nonrepeating_from_set(string):
    for i in string:
        if string.count(i) == 1:
            s.add(i)
            return i
    return None
print(first_nonrepeating_from_set('abcd'))
print(s)
print(first_nonrepeating_from_set('karan'))
print(s)
print(first_nonrepeating_from_set('suraksha'))
print(s)
