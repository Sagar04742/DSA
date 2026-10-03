arr = [5, 2, 8, 1, 9,8.5]


def second_largest(arr):
    f,s = arr[0] , 0
    for i in range(len(arr)):
        if arr[i] >= f:
            f , s = arr[i] , f
        elif arr[i] >= s and arr[i] < f:
            s = arr[i]
    
    print(s)
    
second_largest(arr)

def newMethod(arr):
    arr.sort()
    second_largest = arr[len(arr) - 2]
    print(second_largest)

newMethod(arr)
    
    
def more_robust(arr):
    f = float("-inf")
    s = float("-inf")
    
    for x in arr:
        if  x > f:
            f,s = x ,f
        elif x > s and x<f:
            s = x
    print(s)
    
more_robust(arr)
    