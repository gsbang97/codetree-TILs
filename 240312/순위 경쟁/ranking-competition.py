#  점수 변동 관련 정보가 주어졌을 때, 명예의 전당에 올라간 사람의 조합이 총 몇 번 바뀌었는지를 출력
n = int(input())
scores = [0,0,0]
rank = 5
next_rank = 0
cnt = 0
for _ in range(n):
    c,s = input().split()
    s = int(s)
    if c == 'A':
        scores[0] += s
    elif c == 'B':
        scores[1] += s
    elif c == 'C':
        scores[2] += s
    next_rank = 0
    max_score = max(scores)
    for i in range(3):
        if max_score == scores[i]:
            next_rank += 2**i
    if next_rank != rank:
        rank = next_rank
        cnt +=1
print(cnt)