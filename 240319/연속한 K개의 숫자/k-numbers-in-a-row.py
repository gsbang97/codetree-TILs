# 1부터 N까지의 숫자들 중 B개 숫자들이 빠져 있습니다. 
# 여기에 연속한 K개의 숫자들이 최소 한 세트는 존재
# 현재 없는 B개의 숫자들 중 추가해야 하는 숫자 개수의 최솟값

n,k,b = map(int, input().split())
cnt_sum = [0 for _ in range(n+1)]
numbers = set([int(input()) for _ in range(b)])
min_cnt = k
for i in range(1,n+1):
    if i in numbers:
        cnt_sum[i] = cnt_sum[i-1]
    else:
        cnt_sum[i] = cnt_sum[i-1] + 1
    if i >= k:
        cnt = cnt_sum[i] - cnt_sum[i-k]
        min_cnt = min(k-cnt, min_cnt)

print(min_cnt)