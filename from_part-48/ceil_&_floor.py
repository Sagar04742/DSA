arr = [5,7,8, 10,11,12, 15,17,18,19]

def ceil(arr,target):
    n = len(arr)
    ceil = n
    floor = n
    low = 0
    high = n-1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target: 
            return [mid,mid]
        elif arr[mid] >= target:
            ceil = mid
            high = mid - 1
        else:
            floor = mid
            low = mid + 1 

    return [floor , ceil ] 

print(ceil(arr,7))
    