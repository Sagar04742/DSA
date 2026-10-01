arr = [1,2,5,6,9,8,4,5,6,2,3,7,5,9,6,2]

def merge_array(left,right):
    result = []
    i,j = 0,0
    n,m = len(left),len(right)
    
    while i<n and j<m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else: 
            result.append(right[j])
            j += 1
    if i<n:
        while i<n:
            result.append(left[i])
            i += 1
    if j<m:
        while j<m:
            result.append(right[j])
            j += 1
    
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_array = merge_sort(arr[:mid])
    right_array = merge_sort(arr[mid:])
    return merge_array(left_array,right_array)

print(merge_sort(arr))