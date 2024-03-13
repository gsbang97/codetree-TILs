# 정수로 이루어진 두 수열을 비교하여 같은 원소를 가지고 있는지 판단
# n : 수열 1 원소의 개수
n = int(input())
# arr1 : 수열 1
arr1 = list(map(int, input().split()))
# m : 수열 2 원소의 개수
m = int(input())
# arr2 : 수열 2
arr2 = list(map(int, input().split()))
set1 = set(arr1)
for i in arr2:
    if i in set1:
        print(1, end=" ")
    else:
        print(0, end=" ")