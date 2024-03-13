# n개의 음이 아닌 정수가 입력으로 주어졌을 때, 그 중 m개의 숫자를 뽑아 모두 xor한 결과의 최댓값을 출력
n,m = map(int, input().split())

numbers = list(map(int, input().split()))

max_value = 0
def choose(cnt, score, last_idx):
    global max_value
    if cnt == m:
        max_value = max(max_value, score)
        return
    if cnt == 0:
        for i in range(n):
            choose(cnt+1, numbers[i],i)
    else:
        for i in range(last_idx+1,n):
            choose(cnt+1, score^numbers[i],i)
choose(0,0,-1)
print(max_value)