# 각각의 위치에 있던 원소가 어느 위치로 이동하는지 출력
n = int(input())

numbers = [(i, int(num)) for i, num in enumerate(input().split(), start = 1)]
num_dict = dict()
numbers.sort(key = lambda x : (x[1],x[0]))
for i,(idx, _) in enumerate(numbers, start = 1):
    num_dict[idx] = i
for i in range(1,n+1):
    print(num_dict[i],end = " ")