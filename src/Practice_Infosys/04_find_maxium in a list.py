lis = [1,2,3,4,5]


def max_list(lis):
    max_value = lis[0]
    for li in lis:
        if li > max_value:
            max_value = li
    return max_value


print(max_list(lis))
print(max(lis))

