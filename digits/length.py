x = 654132

# print(len(str(x)))

#------------------------------------

# count = 0 
# for i in range(len(str(x))):
#     count += 1
# print(count)

#------------------------------------

# count = 0
# num = x

# while num>0:
#     count += 1
#     num = num //10
# print(count)

#------------------------------------

from math import *

def digitCount(x):
    return int(log10(x)+1)

print(digitCount(x))