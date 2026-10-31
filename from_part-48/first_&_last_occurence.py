arr = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5, 6]

def first(arr, target):
    lb = -1
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb


def last(arr, target):
    ub = len(arr)
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub - 1


def FirstAndLastOccurrence(arr, target):
    f = first(arr, target)

    if f == -1 or arr[f] != target:
        return [-1, -1]

    return [f, last(arr, target)]


print(FirstAndLastOccurrence(arr, 5))   # [7, 11]
print(FirstAndLastOccurrence(arr, 2))   # [1, 3]
print(FirstAndLastOccurrence(arr, 0))   # [-1, -1]
print(FirstAndLastOccurrence(arr, 10))  # [-1, -1]