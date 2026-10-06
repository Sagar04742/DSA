arr = [14, 3, 22, 7, 19, 5, 31, 12, 26, 9]
P = 41

# Find the two numbers in arr whose sum is P

# def TwoSum(arr,p):
#     for i in range(len(arr)):
#         for j in range(i+1 , len(arr)):
#             if arr[i] + arr[j] == p:
#                 return i ,j 
            
def TwoSum(arr,target):
    seen = {}
    for i in range(len(arr)):
        needed = target - arr[i]
        if needed in seen:
            return seen[needed] , i
        seen[arr[i]] = i
print(TwoSum(arr,P))