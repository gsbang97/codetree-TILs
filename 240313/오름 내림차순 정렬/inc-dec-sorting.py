# n: 원소의 수
n = int(input())
arr = list(map(int, input().split()))

# 오름차순 출력
print(*sorted(arr))
print(*sorted(arr,reverse = True))