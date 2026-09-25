x = 112211

# def reverse(x):
#     new = 0
#     while x >0:
#         new = new*10 + (x%10)
#         x =x//10
#     return new
    
# def isPallindrome(x):
#     if x == reverse(x):
#         print("Yes")
#     else: print("No")

# isPallindrome(x)


def pal(num):
    n = len(str(num))
    for i in str(num):
        if int(i) == num[n-1]:
            n -= 1
        else:
            return "Not"
    return "Yes"

print(pal(x))

