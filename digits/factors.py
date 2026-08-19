from math import sqrt
x = 36
result = []

for i in range(1,int(sqrt(x))+1):
    if x % i ==0:
        result.append(i)
        if (x//i != i):
            result.append(x//i)

result.sort()
print(result)
            
            