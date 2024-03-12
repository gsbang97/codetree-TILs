# n개의 숫자를 적당한 순서에 맞춰 나열하여 각 숫자들을 붙였을 때 나올 수 있는 숫자 중 가장 큰 값
from functools import cmp_to_key

n = int(input())
numbers = [int(input()) for _ in range(n)]

def compare(x,y):
    if int(str(x)+str(y)) > int(str(y)+str(x)):
        return -1
    elif int(str(x)+str(y)) < int(str(y)+str(x)):
        return 1
    else:
        return 0

numbers.sort(key = cmp_to_key(compare))
s = ''
for i in numbers:
    s += str(i)
print(s)