from functools import cmp_to_key

def compare(x,y):
    xy = int(x+y)
    yx = int(y+x)
    if xy > yx:
        return -1
    elif yx > xy:
        return 1
    else:
        return 0

n = int(input())
numbers = [input() for _ in range(n)]
numbers.sort(key = cmp_to_key(compare))

print("".join(numbers))