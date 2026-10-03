arr = [5, 2, 8, 8, 1, 9, 9, 8.5, 5, 2]

def removeDuplicatesFromSorted(arr):
    i = 0
    while i < len(arr) -1:
        if arr[i] == arr[i+1]:
            arr.pop(i+1)
        else:
            i += 1
    print(arr)

def removeDuplicatesFromUnsorted(arr):
    unique = set()
    i = 0
    while i < len(arr):
        if arr[i] in unique:
            arr.pop(i)
        else:
            unique.add(arr[i])
            i += 1
    print(arr)
    
removeDuplicatesFromUnsorted(arr)    

removeDuplicatesFromSorted(arr)