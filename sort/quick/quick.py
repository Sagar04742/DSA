arr = [1,2,5,4,6,9,8,7,5,3,2,6,5,4,9,5]

def partition(arr,low,high):
    pivot = arr[low]
    i,j = low , high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
            
        if i < j:
            arr[i] , arr[j] = arr[j] , arr[i]
        else:
            arr[low] , arr[j] = arr[j] , arr[low]
            break
    return j
            
def quick_sort(arr,low,high):
    if low < high:
        pivot = partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)
        
quick_sort(arr,0,len(arr)-1)
print(arr)