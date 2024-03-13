# n개의 숫자가 주어졌을 때, 서로 다른 숫자의 수를 출력
# n : 원소의 개수
n = int(input())
arr = set(map(int,input().split()))

print(len(arr))