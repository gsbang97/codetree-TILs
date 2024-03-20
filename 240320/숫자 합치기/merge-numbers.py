from heapq import heappop, heappush

n = int(input())
numbers = []
for number in map(int, input().split()):
    heappush(numbers, number)
ans = 0
while numbers:
    A = heappop(numbers)
    if numbers:
        B = heappop(numbers)
        ans += A + B
        heappush(numbers, A + B)
print(ans)