n = "nitin"

def isPalindrome(str,left,right):
    if left >= right:
        return "Yes"
    elif str[left] == str[right]:
        return isPalindrome(str,left+1,right-1)
    return "No"


print(isPalindrome(n,0,len(n)-1))









# def isPalindrome(str):
#     n = len(str)
#     for i in (range(n//2)):
#         if str[i] != str[n-1]:
#             return "No"
#         else:
#             n -= 1    
#     return "Yes"

# print(isPalindrome(n))