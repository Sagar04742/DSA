x = 112211

def reverse(x):
    new = 0
    while x >0:
        new = new*10 + (x%10)
        x =x//10
    return new
    
def isPallindrome(x):
    if x == reverse(x):
        print("Yes")
    else: print("No")

isPallindrome(x)




