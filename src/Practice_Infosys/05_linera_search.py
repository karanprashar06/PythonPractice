



def linear_search(arr,target):
    for num in arr:
        if num == target:
            return num,arr.index(target)
    return -1
print(linear_search([1,22,6,4,5],4))




def linear_search1(arr,target):
    for num in range(len(arr)):
        if arr[num] == target:
            return num
    return -1
print(linear_search1([1,22,6,4,5],22))






def linear_search2(arr,target):
        try:
            return arr.index(target)
        except ValueError:
            return -1


print(linear_search2([1,22,6,4,5],22))