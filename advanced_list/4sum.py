arr = [ 1 , 0 , -1 , 0 , -2 , 2]

def FourSum(arr):
    arr.sort()
    result = []
    
    for i in range(len(arr)):
        left = i + 1 
        secondLeft = left + 1 
        right = len(arr) - 1
        
        while left < right :
            total = arr[i] + arr[left] + arr[secondLeft] + arr[right] 
            
            if secondLeft < right:
                if total < 0 :
                    secondLeft += 1
                elif total > 0 :
                    right -= 1
                else:
                    if [arr[i] , arr[left] , arr[secondLeft] , arr[right] ] not in result:
                            result.append([arr[i] , arr[left] , arr[secondLeft] , arr[right] ])
                    secondLeft += 1
                    right -= 1
            else:
                left += 1
                secondLeft = left + 1
                right = len(arr) - 1 
        
    print(result)

            
FourSum(arr)
                