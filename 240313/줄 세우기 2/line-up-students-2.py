n = int(input())

students = [list(map(int, input().split())) + [i] for i in range(1,n+1)]

students.sort(key = lambda x : (x[0], -x[1]))

for student in students:
    print(*student)