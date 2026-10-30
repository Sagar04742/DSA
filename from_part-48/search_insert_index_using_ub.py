arr = [1,3,4,5,6,8,9,12,15]

def searchInsert(arr,target):
    low = 0
    high = len(arr) - 1
    
    ub = len(arr)
    
    
    while low<=high:
        mid = (low+high) //2 

        if arr[mid] > target:
            ub = mid
            high = mid -1
        elif arr[mid] < target:
            low = mid +1
        else:
            return f"Item already present at {mid}"
    
    return f'Insert position at index {ub}'

print(searchInsert(arr,2))
            