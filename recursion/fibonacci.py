# def func(num):
#     if num==0 or num==1:
#         return num
#     return func(num-1) + func(num-2)

# def fibonacci(nth):
#     answer = func(nth)
#     return answer

# print(fibonacci(6))

def func(num):
    count = 0
    arr = []

    while count < num:
        if count == 0 or count == 1:
            arr.append(count)
        else:
            arr.append(arr[count - 1] + arr[count - 2])

        count += 1

    return arr


def fibonacci(n):
    answer = func(n)
    return answer


print(fibonacci(5))

    
fibonacci(5)
