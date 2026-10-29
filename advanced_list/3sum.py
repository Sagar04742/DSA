arr = [ -1 , 0 , 1 , 2 , -1 , -4 ] 

def threeSum(arr):
    arr.sort()
    result = []
    count = 0 
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    if [arr[i] , arr[j] , arr[k]] not in result:
                        result.append([arr[i] , arr[j] , arr[k] ])
    
    print(result)
    
threeSum(arr)