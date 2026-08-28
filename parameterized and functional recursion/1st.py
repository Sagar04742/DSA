def sumtoNdigits(sum,i,n):
    if i>n:
        print(sum)
        return
    sumtoNdigits(sum+i,i+1,n)

sumtoNdigits(0,1,10)