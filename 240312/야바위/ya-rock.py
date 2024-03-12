N = int(input())
# a번 종이컵과 b번 종이컵을 교환한 뒤, c번 종이컵을 열어 그 안에 조약돌이 있으면 점수를 얻는 행동
behaviors = [tuple(map(int, input().split())) for _ in range(N)]
max_score = 0
for i in range(3):
    stone = [False]+[i==j for j in range(3)]
    score = 0
    for a,b,c in behaviors:
        tmp = stone[a]
        stone[a] = stone[b]
        stone[b] = tmp
        if stone[c]:
            score +=1
    max_score = max(score, max_score)
print(max_score)