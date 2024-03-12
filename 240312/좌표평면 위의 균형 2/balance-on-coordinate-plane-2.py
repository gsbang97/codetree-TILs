# 좌표평면 위에 N개의 점
# x축과 y축에 평행한 직선을 정확히 1개씩 그어 좌표평면을 4군데로 분할하여 균형 있게 나누려고합니다
# 4군데 중 가장 많은 점의 수가 최소가 되도록 하는 것을 의미
# x축과 y축에 평행한 직선은 항상 짝수
# M : 가장 많은 수의 점이 있는 구역의 점의 개수
# M의 최소값을 구하는 프로그램

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
min_score = 100
for x in range(2,101,2):
    for y in range(2,101,2):
        # 
        score = [0,0,0,0]
        for px,py in points:
            if px < x and py < y:
                score[0] += 1 
            elif px < x and py > y:
                score[1] += 1 
            elif px > x and py < y:
                score[2] += 1 
            else:
                score[3] += 1 
        min_score = min(min_score, max(score))
print(min_score)