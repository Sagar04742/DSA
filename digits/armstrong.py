from math import pow
x = 153

# def isArmstrong(num):
#     sum = 0
    
#     n = len(str(x))
#     for i in range(n):
#         sum += pow(num[i],n)
#     if num == sum:
#         return "Yes"
#     else:
#         return "No"

# print(isArmstrong(x))

def isArmstrong(num):
    n = len(str(num))
    sum = 0
    while num >0:
        sum = sum + pow(num%10,n)
        num = num //10
    if sum == x:
        return True
    else: 
        return False

if(isArmstrong(x)):
    print("Yes")
else:
    print("No")