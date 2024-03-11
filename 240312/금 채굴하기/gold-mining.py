n, cost = map(int, input().split())
gold_mat = [list(map(int, input().split())) for _ in range(n)]
max_gold = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            k_cost = k*k+(k+1)*(k+1)
            gold = 0
            for l in range(k+1):
                
                j_1 = j - k - l
                j_2 = j + k - l + 1
                if j_1 < 0:
                    j_1 = 0
                if j_2 > n :
                    j_2 = n
                if l == 0:
                    gold += sum(gold_mat[i][j_1:j_2])
                else:
                    if i+l < n:
                        gold += sum(gold_mat[i+l][j_1:j_2])
                    if i-l >= 0 :
                        gold += sum(gold_mat[i-l][j_1:j_2])
                # if (k == 1) and i == 2 and j == 4:
                #     print(i,l,j_1,j_2)
            if gold*cost >= k_cost:
                max_gold = max(max_gold, gold)
            # if (k == 1) and i == 2 and j == 4:
            #     print(gold, cost, k_cost,gold*cost >= k_cost, max_gold,max(max_gold, gold))
print(max_gold)