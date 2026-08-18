x = 12345


def reverse(x):
    new = 0
    while x>0:
        new = new*10 + (x%10)
        x = x//10
    return new

print(reverse(x))