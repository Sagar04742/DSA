arr = [1,2,3,4,5,6,7,8,9]

# n = len(arr)
# for i in range(len(arr)//2):
#     temp = arr[i]
#     arr[i] = arr[n-1]
#     arr[n-1] = temp
#     n -= 1
# print(arr)

# USING RECURSION  

# def reverseArray(ar, left, right):
#     if left >= right:
#         return ar
#     ar[left], ar[right] = ar[right], ar[left]
#     return reverseArray(ar, left + 1, right - 1)
# print(reverseArray(arr, 2, 5))

#  USING WHILE LOOP

def reverseArray(newArr,left,right):
    while left <= right:
        newArr[left], newArr[right] = newArr[right], newArr[left]
        return reverseArray(newArr,left+1,right-1)
    return newArr
print(reverseArray(arr,2,5))
        

reverseArray(arr,2,5)