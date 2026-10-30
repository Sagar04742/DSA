arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Binary_search(target, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if target < arr[mid]:
            high = mid - 1

        elif target > arr[mid]:
            low = mid + 1

        else:
            return f"Target found at index {mid}"

    return "Target not found"

print(Binary_search(4, arr))
