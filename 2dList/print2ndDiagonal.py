arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def print2ndDiagonal(arr):
        
    rows = len(arr)
    cols = len(arr[0])
    
    count = len(arr[0]) - 1
    
    for i in range(rows):
        for j in range(cols):
            if j !=  count:
                arr[i][j] = "*"
                continue
            count -= 1

    print(arr)
    
print2ndDiagonal(arr)    