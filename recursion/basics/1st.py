

def printName(name,count):
    if count <= 4:
        print(name)
        printName(name, count+1)
    else:
        return 
    
printName("Sagar",1)    