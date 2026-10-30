arr= [1,1,2,3,4,4,6,7,8,11,12,12]

def lowerBound(arr,target):
    low = 0
    high = len(arr) - 1
    lb = -1
    
    while low <= high:
        mid = (low+high) // 2
        
        if arr[mid] >= target:
            lb = mid
            high = mid-1
        else:
            low = mid +1
        
    return lb

print(lowerBound(arr,4))