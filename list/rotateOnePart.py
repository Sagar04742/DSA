arr = [1,2,3,4,5,6,7,8,9]

def rotate(arr,left,right,k):
    
    k = k % (right - left + 1)
    r = 0
    while r < k:
        last = arr[right-1]
        for j in range(right-2,left-2,-1):
            arr[j+1] = arr[j]
        arr[left-1] = last
        r += 1
    
    print(arr)
    
rotate(arr,1,5,2)
        
        