arr = [ 1,2,3,4,5,6,7,8,9]

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i+1,n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[max_index] , arr[i] = arr[i] , arr[max_index]
    
    print(arr)
    
selectionSort(arr)        
            
