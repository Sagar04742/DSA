arr = [1,2,3,4,5,6,7,8,9]

def rotateArray(arr,r):
    k = r % len(arr)
    while k!=0:
        last = arr[len(arr)-1]
        j = len(arr)-2
        while j >=0:
            arr[j+1] = arr[j]
            j -= 1
        arr.pop(0)
        arr.insert(0,last)
        
        k-=1
    print(arr)

rotateArray(arr,2)