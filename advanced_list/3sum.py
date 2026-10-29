arr = [ -1 , 0 , 1 , 2 , -1 , -4 ] 

def ThreeSum(arr):
    arr.sort()
    result = []
    
    for i in range(len(arr)):
        
        first = arr[i]
        left = i+1
        right  = len(arr) - 1
        
        while left < right:
            total = first + arr[left] + arr[right]
            if  total == 0:
                if [first , arr[left] , arr[right]] not in result:
                    result.append([first , arr[left] , arr[right]])
                    
                left += 1
                right -= 1
                    
            elif total < 0:
                left += 1
            elif total > 0:
                right -= 1
                
    print(result)

ThreeSum(arr)


# def threeSum(arr):
#     arr.sort()
#     result = []
#     count = 0 
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             for k in range(j+1,len(arr)):
#                 if arr[i] + arr[j] + arr[k] == 0:
#                     if [arr[i] , arr[j] , arr[k]] not in result:
#                         result.append([arr[i] , arr[j] , arr[k] ])
    
#     print(result)
    
# threeSum(arr)