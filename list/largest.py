arr = [11,2,55,69,-51,105,24,95]

def findLargestNum(arr):
    larg_index = 0
    for i in range(len(arr)):
        if arr[i] > arr[larg_index]:
            larg_index = i
    print(arr[larg_index])
        
findLargestNum(arr)