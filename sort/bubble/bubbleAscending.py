arr = [4,5,1,2,3,6,9,8,5,1]

def bubbleSorrt(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    print(arr)
    
bubbleSorrt(arr)
        