arr = [1,3,4,5,6,8,9,12,15]


def searchInsert(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1

    return low

print(searchInsert(arr,2))