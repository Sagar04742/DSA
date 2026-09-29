arr = [4,5,1,2,3,6,9,8,5,1]

def bubbleSorrt(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-1-i):
            if arr[j] < arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                swapped = True
        if not swapped:
            break
    print(arr)

bubbleSorrt(arr)
        