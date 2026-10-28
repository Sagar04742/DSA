matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 0]
]

rows = len(matrix)
cols = len(matrix[0])

row_of_0 = []
cols_of_0 = []

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            row_of_0.append(i)
            cols_of_0.append(j)

for i in range(rows):
    if i in row_of_0:
        for j in range(cols):
            matrix[i][j] = 0
    for j in range(cols):
        if j in cols_of_0:
            matrix[i][j] =0
            
print(matrix)
        
                    















# rows = len(matrix)
# cols = len(matrix[0])

# row_i = []
# col_i = []

# for i in range(rows):
#     for j in range(cols):
#         if matrix[i][j] == 0:
#             row_i.append(j)
#             col_i.append(i)
# for i in range(rows):
#     for j in range(cols):
#         if i in row_i:
#             matrix[i][j] =0
        
#         elif j in col_i:
#             matrix[i][j] = 0
        
# print(matrix)
        