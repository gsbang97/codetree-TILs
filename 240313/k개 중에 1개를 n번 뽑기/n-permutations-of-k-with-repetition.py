# 1이상 K이하의 숫자를 하나 고르는 행위를 N번 반복
K, N = map(int, input().split())

def print_ans(answer):
    print(*answer)
def choose(idx,answer):
    if idx == 0:
        print_ans(answer)
        return
    for i in range(1,K+1):
        choose(idx-1, answer +[i])
        
    
choose(N,[])