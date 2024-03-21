import heapq

n = int(input())
strings = []
for _ in range(n):
    string = input()
    left = 0
    right = 0
    score = 0
    for char in string:
        if char == "(":
            left += 1
        if char == ")":
            right += 1
            score += left
    heapq.heappush(strings, (-left,right,score))
lefts = 0
# rights = 0 
ans = 0
for _ in range(n):
    left, right, score = heapq.heappop(strings)
    if right > 0:
        # rights += right
        ans += lefts * right
    lefts -= left
    ans += score
print(ans)