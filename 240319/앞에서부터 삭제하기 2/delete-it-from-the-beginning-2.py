import heapq
from collections import deque

n = int(input())
numbers = deque(map(int, input().split()))

sum_number = sum(numbers)
que = []
for k in range(1,n-2):
    sum_number -= numbers.popleft()
    avr = (sum_number - min(numbers)) / (n - k - 1)
    heapq.heappush(que,-avr)
print(f"{-heapq.heappop(que):.2f}")