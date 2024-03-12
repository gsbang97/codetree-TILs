n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
cnt = 0
for i in range(n-1,-1,-1):
    if sorted_arr[i] != arr[i]:
        cnt = i
        break
print(cnt)