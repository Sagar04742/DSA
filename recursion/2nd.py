def printNtimes(x,y):
    if y ==0:
        return 
    print(x)
    y -= 1
    printNtimes(x,y)
    
printNtimes(15,6)
        