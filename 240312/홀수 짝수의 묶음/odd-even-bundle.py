# N개의 숫자들이 주어지면 주어진 숫자들을 전부 사용
# 합이 짝수 -> 홀수 -> 짝수... 짝수가 홀수가 번갈아 나오게 묶어야함
# 주어진 순서에 상관없이 묶음을 만들어도 된다?
N = int(input())
numbers = list(map(int, input().split()))

num1 = 0
num2 = sum(numbers)
is_odd = False
cnt = 0
for i in range(N):
    num1 += numbers[i]
    num2 -= numbers[i]
    if is_odd:
        if num1%2 == 1 and num2%2 == 0:
            cnt += 1
            num1 = 0
    else:
        if num1%2 == 0 and num2%2 == 1:
            cnt += 1
            num1 = 0
print(cnt)