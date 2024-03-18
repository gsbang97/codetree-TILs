import heapq
from collections import deque

n = int(input())
numbers = deque(map(int, input().split()))

sum_number = sum(numbers)
min_number = min(numbers)
que = []
for k in range(1,n-2):
    value = numbers.popleft()
    sum_number -= value
    if value == min_number:
        min_number = min(numbers)
    avr = (sum_number - min_number) / (n - k - 1)
    heapq.heappush(que,-avr)
print(f"{-heapq.heappop(que):.2f}")