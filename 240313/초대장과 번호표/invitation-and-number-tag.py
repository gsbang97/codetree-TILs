# n : 사람 수 (번호표), g : 그룹수 
# 사람들에게 초대장을 나눠주려 하는데, 그룹 인원수가 k인 그룹에서 k-1명의 사람들이 초대장을 받았다면 나머지 한 사람도 무조건 초대장을 받아야합니다. 1번 사람에게는 무조건 초대장을 준다고 할 때, 확실하게 초대장을 받게 되는 인원 수를 구하는 프로그램을 작성하세요.
n,g = map(int, input().split())
num_c = 0
invites = set([1])
num_n = 1
groups = [list(map(int, input().split()))[1:] for _ in range(g)]
while(num_c != num_n):
    num_c = len(invites)
    for g in groups:
        for i in invites:
            if i in g:
                g.remove(i)
        if len(g) == 1:
            invites.add(g[0])
    num_n = len(invites)

print(len(invites))