matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def transpose(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(i+1 ,n):
            matrix[i][j] , matrix [j][i] =  matrix [j][i] , matrix[i][j]
    return arr

def rotateBy90deg(arr):
    matrix = transpose(arr)
    
    for i in range(0,len(matrix)):
        matrix[i].reverse()
        
    print(matrix)
    
rotateBy90deg(matrix)



# def rotateBy90deg(arr):
#     result = [
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
#     ]
#     rows = len(arr)
#     cols = len(arr[0])

#     for i in range(rows):
#         for j in range(cols):
#             result[j][(len(arr) -1)-i] = arr[i][j]
    
#     print(result)
    
# rotateBy90deg(matrix)