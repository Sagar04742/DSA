arr = [1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0]

def maxOnes(arr):
    max = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            count = 1
            j = i + 1
            while j < len(arr):
                if arr[j] == 1:
                    count += 1
                    j += 1
                else:
                    break
            if count > max:
                max = count
        
    return max

def optinal(arr):
    maxOnes = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            maxOnes = max(maxOnes,count)
            count = 0
    
    maxOnes = max(maxOnes,count)

    return maxOnes

print(maxOnes(arr))
            