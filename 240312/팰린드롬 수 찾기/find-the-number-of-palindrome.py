# X이상 Y이하의 값 중 팰린드롬의 개수
# 팰린드롬 : 거꾸로 읽어도 제대로 읽는 것과 같은 수 ( 34543, 9009 등)

X,Y = map(int, input().split())
cnt = 0
for i in range(X,Y+1):
    i = str(i)
    is_fel = True
    for idx in range(len(i)//2):
        if i[idx] != i[-1-idx]:
            is_fel = False
            break
    if is_fel:
        cnt +=1


print(cnt)