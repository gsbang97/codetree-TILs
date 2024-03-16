# N개의 원소로 이루어진 수열 A
# M개의 숫자로 이루어진 수열 B

# 아름다운 수열 : 수열 B의 각 원소들에 동일한 숫자를 더하거나 빼고 순서를 바꿔 나오는 수열
# 수열 A에서 길이가 M인 연속 부분 수열들 중 아름다운 수열의 수를 세는 프로그램

n = int(input())
A = [int(input()) for _ in range(n)]
m = int(input())
B = set([int(input()) for _ in range(m)])
buty = []
# print(A)
# print(B)
# for i in range(n-m+1):
i = 0
while i <= n-m:
    # setA = set(A[i:i+m])
    is_buty = True
    if A[i] in B:
        for a in A[i:i+m]:
            if a not in B:
                is_buty = False
                break
    else:
        is_buty = False
    if is_buty:
        # print('pure')
        # print(A[i:i+m],i)
        buty.append(i)
        i += m
    else:
        numbers = [b-A[i] for b in B]
        # print(numbers)
        for number in numbers:
            flag = True
            for a in A[i:i+m]:
                if a+number not in B:
                    flag = False
                    break
            if flag:
                # print('plus')
                # print(A[i:i+m],i)
                buty.append(i)
                i += m
                break
        if flag == False:
            i += 1
print(len(buty))
for b in buty:
    print(b+1)