n = int(input())

students = [input().split()+ [i] for i in range(1,n+1)]

students.sort(key=lambda x : (-int(x[0]),-int(x[1]),x[2]))

for student in students:
    print(*student)