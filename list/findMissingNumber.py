arr = [ 1, 0 ,3,4]

def missingNumber(arr):
    i = 0 
    while i <= len(arr):
        if i in arr:
            i += 1  
        else:
            return i

    return "No missing numbers"

print(missingNumber(arr)  )
        
        