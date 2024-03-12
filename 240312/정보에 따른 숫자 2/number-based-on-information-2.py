# 특정 위치 x = k로부터 가장 가까이에 있는 알파벳 S까지의 거리 d1이 
# x = k로부터 가장 가까이에 있는 알파벳 N까지의 거리 d2보다 같거나 작은 경우 
# x = k는 특별한 위치가 됩니다. 
# x = a부터 x = b까지의 위치 중 특별한 위치의 수를 구하는 프로그램
T,a,b = map(int, input().split())
# ( 알파벳 값 c, 해당 알파벳이 놓여있는 위치 x값)
loc = [tuple(input().split()) for _ in range(T)]
cnt = 0
for i in range(a,b+1):
    d1 = 1000
    d2 = 1000
    for c,x in loc:
        x = int(x)
        if c == 'S':
            d1 = min(abs(i-x),d1)
        else:
            d2 = min(abs(i-x),d2)
    if d1 <= d2 :
        cnt +=1
print(cnt)