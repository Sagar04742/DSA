arr = [1,99,2,5,3,100,98,4,101,6]

def longestConsecutive(arr):
    arr.sort()
    
    max_count = 1
    count = 1 
    for i in range(len(arr) - 1):
        if arr[i + 1] == arr[i] + 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
    return max(max_count, count)

print(longestConsecutive(arr))


def longestConsecutiveUsingSet(arr):
    numbers = set(arr)
    longest = 0

    for number in numbers:
        if number - 1 not in numbers:
            length = 1
            while number + length in numbers:
                length += 1
            longest = max(longest, length)

    return longest