arr  = [-2,1,3,-4,5,1,-3,6,-2]

# def maxSubarray(arr):
#     n = len(arr)
#     max_sum = float("-inf")
#     for i in range(n):
#         sum = arr[i]
#         if arr[i] > max_sum:
#             max_sum = arr[i]
#         for j in range(i+1,n):
#             sum +=  arr[j]
#             if sum > max_sum:
#                 max_sum = sum
                
#     return max_sum

# print(maxSubarray(arr))

def max_sum(arr):
    sum = arr[0]
    maxSum = arr[0]
    for i in range(1,len(arr)):
        sum = max(arr[i] , sum + arr[i])
        maxSum = max(maxSum,sum)
    return maxSum

print(max_sum(arr))