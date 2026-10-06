arr1 = [ 1,1,1,1, 3, 5, 7, 9]
arr2 = [ 2, 4,4,4,5, 6, 8, 10] 

def merge2arrays(arr1,arr2):
    n , m = len(arr1) , len(arr2)
    i ,j = 0 , 0
    result = []

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
        else:
            if not result or result[-1] != arr1[i]:
                 result.append(arr1[i])
            i += 1
            j += 1
            

    while i < n:
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1
    
    while j < m:
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1
            
    print(result)

merge2arrays(arr1,arr2)