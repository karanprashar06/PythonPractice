


def linear_sort(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


print(linear_sort([1,2,3,3,4,66,4,3],66))


