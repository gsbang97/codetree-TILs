from heapq import heappop, heappush

n = int(input())

numbers = list(map(int, input().split()))
min_numbers = []
max_number = 0
# max_numbers = []
ans = 1
for i, number in enumerate(numbers):
    if i < 3:
        heappush(min_numbers, -number)
        ans *= number
        if i < 2:
            print(-1)
        else:
            max_number = -heappop(min_numbers)
            print(ans)
    else:
        if max_number > number:
            ans = ans * number // max_number
            heappush(min_numbers, -number)
            max_number = -heappop(min_numbers)
        print(ans)