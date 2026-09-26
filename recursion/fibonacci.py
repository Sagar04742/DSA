def func(num):
    if num==0 or num==1:
        return num
    return func(num-1) + func(num-2)

def fibonacci(nth):
    answer = func(nth)
    return answer

print(fibonacci(6))