# N개의 숫자들이 주어지면 주어진 숫자들을 전부 사용
# 합이 짝수 -> 홀수 -> 짝수... 짝수가 홀수가 번갈아 나오게 묶어야함
# 주어진 순서에 상관없이 묶음을 만들어도 된다?
N = int(input())
numbers = list(map(int, input().split()))
odd = [0,0]
for n in numbers:
    if n % 2 == 0:
        odd[1] +=1
    else:
        odd[0] +=1
if odd[0] < odd[1]: # 짝수가 더 많은 경우
    print(odd[1]*2 + 1)
elif odd[0] == odd[1]: # 짝수와 홀수 수가 같은 경우
    print(odd[1]*2)
else: # 홀수가 더 많은 경우
    diff = odd[0] - odd[1]
    cnt = 0
    while(diff > 4):
        diff -= 3
        cnt += 2
    if diff == 4 or diff == 2:
        cnt += 1
    elif diff == 3:
        cnt += 2
    print(cnt)