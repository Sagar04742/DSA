def sumOfNo(n):
    if n==1:
        return 1
    return  n + sumOfNo(n-1)
    
print(sumOfNo(10))