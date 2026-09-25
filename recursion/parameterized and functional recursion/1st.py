def sumOfDigits(sum,i,n):
    if i > n:
        print(sum)
        return
    sumOfDigits(sum+i,i+1,n)
    
    
sumOfDigits(0,1,4)