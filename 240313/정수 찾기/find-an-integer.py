# 수열 a와 수열 b가 주어졌을 때, 수열 b의 각 원소가 수열 a에 포함되는지 알아보는 프로그램
# n : 수열 a의 원소의 개수, m : 수열 b의 원소의 개수
n = int(input())
a = set(input().split())
m = int(input())
for i in input().split():
    if i in a:
        print(1)
    else: 
        print(0)