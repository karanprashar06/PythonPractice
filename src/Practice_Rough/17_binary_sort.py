


def binary_sort(arr, target):
    right =0
    left =len(arr)-1

    while right <= left:
        mid =(right+left)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            right = mid+1
        else:
            left = mid-1

    return -1

print(binary_sort([1,2,3,3,4,66,4,3],66))