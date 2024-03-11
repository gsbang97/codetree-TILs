n = int(input())
numbers = [int(input()) for _ in range(n)]
result = -1
for i in range(n-2):
    s = 0
    for j in range(i+1, n-1):
        # print(numbers[i],numbers[j])
        min_idx = min(len(str(numbers[i])),len(str(numbers[j])))
        is_carry = False
        for sq in range(min_idx):
            idx = 10**sq
            # print(idx,(numbers[i]//idx)%10 , (numbers[j]//idx)%10,((numbers[i]//idx)%10 + (numbers[j]//idx)%10) >9)
            if ((numbers[i]//idx)%10 + (numbers[j]//idx)%10) > 9:
                is_carry = True
                break
        # print(is_carry)
        if not is_carry:
            # print(range(j+1, n))
            for k in range(j+1, n):
                # print(numbers[i],numbers[j], numbers[k])
                s = numbers[i] + numbers[j]
                min_idx = min(len(str(s)),len(str(numbers[k])))
                is_carry = False
                for sq in range(min_idx):
                    idx = 10**sq
                    # print(idx,(s//idx)%10 , (numbers[k]//idx)%10)
                    if (s//idx)%10 + (numbers[k]//idx)%10 >9:
                        is_carry = True
                        break
                if is_carry:
                    continue
                s += numbers[k]
                result = max(result,s)

print(result)