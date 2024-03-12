N = int(input())

seat = input()

min_diff = 1000
max_diff = 0
start = -1
# end = -1
for i,s in enumerate(seat):
    if s == '1':
        if start == -1:
            start = i
        else:
            dist = i - start
            max_diff = max(max_diff, dist)
            min_diff = min(min_diff, dist)
            start = i
max_diff = max(max_diff//2, N-start-1)
print(min(min_diff, max_diff))