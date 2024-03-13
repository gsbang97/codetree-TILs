n = int(input())
numbers = list(map(int, input().split()))
for i in range(1,n+1,2):
    sorted_number = sorted(numbers[:i])
    print(sorted_number[i//2], end=" ")