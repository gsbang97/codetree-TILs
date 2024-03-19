n,q = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()
min_point = numbers[0]
max_point = numbers[-1]
prefix_sum = [0 for _ in range(max_point-min_point + 2)]
for num in numbers:
    prefix_sum[num-min_point+1] = 1
for i in range(1,max_point-min_point+2):
    if prefix_sum[i] == 1:
        prefix_sum[i] = prefix_sum[i-1] + 1
    else:
        prefix_sum[i] = prefix_sum[i-1]
# print(prefix_sum)

for _ in range(q):
    a,b = map(int, input().split())
    a_value = b_value = 0
    if a > max_point:
        print(0)
        continue
    elif a <= min_point:
        a_value = 0
    else:
        a_value = prefix_sum[a-min_point]
    if b < min_point:
        print(0)
        continue
    elif b >= max_point:
        b_value = n
    else:
        b_value = prefix_sum[b-min_point+1]
    print(b_value-a_value)