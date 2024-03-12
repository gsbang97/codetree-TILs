# 특정 위치를 골라 해당 위치의 블럭을 다른 위치로 옮기는 작업을 반복
# 모든 위치에 놓인 블럭의 개수가 동일해지게 만듬
# 움직여야 할 최소 블럭의 수를 구하는 프로그램 (항상 가능함을 가정)

N = int(input())
blocks = [int(input()) for _ in range(N)] 
avr = sum(blocks)//N
# blocks.sort()
cnt = 0
for i in range(N):
    if blocks[i] > avr:
        cnt += blocks[i] - avr
print(cnt)