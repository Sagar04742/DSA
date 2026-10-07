arr = [1, 2, -2, 4, -1, -2]

def rearrange(arr):
    positives = []
    negetives = []
    result = []
    for i in arr:
        if i > 0:
            positives.append(i)
        else:
            negetives.append(i)
    j,k =0,0
    while j < len(positives) and k < len(negetives):
        result.append(positives[j])
        j += 1
        
        result.append(negetives[k])
        k+=1
    while j < len(positives):
        result.append(positives[j])
        j += 1
    while k < len(negetives):
        result.append(negetives[k])
        k+=1
    
    return result

def optimal(arr):
    result = [0]*len(arr)
    
    pos , neg = 0 , 1
    
    for i in arr:
        if i > 0:
            result[pos] = i
            pos += 2
        else:
            result[neg] = i
            neg += 2
            
    return result

print(optimal(arr))
print(rearrange(arr))