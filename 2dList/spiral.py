arr= [
        [1,2,3,4],
        [12,13,14,5],
        [11,16,15,6],
        [10,9,8,7]
    ]

def SpiralLise(arr):
    
    n = len(arr)
    result = []
    
    left , top = 0 , 0
    right , bottom = n -1 , n -1 
    
    while top <= bottom and left <= right:
        for i in range(left,right+1):
            result.append(arr[top][i])
        top += 1
        
        for i in range(top , bottom + 1):
            result.append(arr[i][right])
        right -= 1
    
        if top <= bottom:
            for i in range(right,left-1, -1 ):
                result.append(arr[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom ,top -1, -1):
                result.append(arr[i][left])
            left += 1
    
    print(result)
    
SpiralLise(arr)