arr = [ 9,8,7,6,5,4,3,2,1]

# def selectionSort(arr):
#     min_ndex = 0
#     j=0
#     while j < len(arr):
#         for i in range(j,len(arr)):
#             if arr[i] < arr[min_ndex]:
#                 min_ndex = i

#         arr[min_ndex] , arr[j] = arr[j] , arr[min_ndex]
        
#         j += 1
#         min_ndex  = j 
    
#     print(arr)
        
# selectionSort(arr)

def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i 
        for j in range(i+1 , len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j 
        arr[min_index] , arr[i] = arr[i] , arr[min_index]
    
    print(arr)

selectionSort(arr)