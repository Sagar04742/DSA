arr = [1,2,0,3,2,0,6,5,0,9,8,2,0,4,0,5,7]

def move0toEnd(arr):
    count = 0
    i = 0
    while i < len(arr):
        if  arr[i] == 0:
            count += 1
            arr.pop(i)
        else:
            i+=1
    if count != 0:
        while count > 0:
            arr.append(0)
            count -= 1
    
    print(arr)

move0toEnd(arr)
            