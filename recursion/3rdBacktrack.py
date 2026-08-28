def printNnumbers(n,i):
    if i==0:
        return 
    printNnumbers(n,i-1)
    print(i)


printNnumbers(5,5)