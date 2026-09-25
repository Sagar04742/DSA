def printNnumbers(n,y):
    if y > n:
        return 
    print(y)
    printNnumbers(n,y+1)

printNnumbers(100,1)