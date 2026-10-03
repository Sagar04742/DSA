arr1 = [1,2,3,4,5,6,7,8,9]
arr2 = [1,2,5,6,4,3,9,8,7]

def isSorted(arr):
    sorted = True
    for x in range(len(arr)-1):
        if arr[x] >= arr[x+1]:
            sorted = False
    if sorted:
        print("Sorted")
    else:
        print("Unsorted")
        

isSorted(arr1)

isSorted(arr2)