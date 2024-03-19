# 테디는 가고 싶은 N 개의 도시들에 스티커
# 최우선적으로 방문하고 싶은 도시에 핀셋을 꽂아뒀습니다.
# 지구본에 여러 행동을 취했습니다. 그의 주요 행동은 다음과 같습니다.

# 핀셋을 꽂은 도시를 현재의 오른쪽 인접 도시로 바꿔서 꽂습니다. 
# 만약 오른쪽에 있는 도시가 없다면 무시합니다.
# 핀셋을 꽂은 도시를 현재의 왼쪽 인접 도시로 바꿔서 꽂습니다. 
# 만약 왼쪽에 있는 도시가 없다면 무시합니다.
# 핀셋이 꽂혀 있는 도시의 오른쪽에 위치한 도시의 스티커를 제거합니다. 
# 만약 오른쪽에 있는 도시가 없다면 무시합니다.
# 핀셋이 꽂혀 있는 도시의 오른쪽에 새로운 도시를 추가하여 스티커를 붙입니다.

# n : 도시들의 수, q : 행동의 수 

class City:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def __str__(self):
        if not( self.left is None or self.right is None):
            if self.left.value == self.right.value:
                return "-1"
            return f"{self.left.value} {self.right.value}"

        return "-1"
def connect_city(c1, c2):
    if c1:
        c1.right = c2
    if c2:
        c2.left = c1
n,q = map(int, input().split())
cities = [City(city) for city in input().split()]
for i in range(n-1):
    connect_city(cities[i],cities[i+1])
connect_city(cities[n-1],cities[0])
tweezer = cities[0]

for i in range(q):
    command = input().split()
    option = int(command[0])
    if option == 1:
        if not tweezer.right is None:
            tweezer = tweezer.right
    elif option == 2:
        if not tweezer.left is None:
            tweezer = tweezer.left
    elif option == 3:
        connect_city(tweezer, tweezer.right.right)
        # if not tweezer.right is None:
        #     tweezer.right = tweezer.right.right
    elif option == 4:
        right = tweezer.right
        connect_city(tweezer, City(command[1]))
        connect_city(tweezer.right, right)
        # print(right.value, tweezer.right.right.value)
        # print(tweezer.right.value, tweezer.right.left.value)
    # print(tweezer, tweezer.value)
    print(tweezer)