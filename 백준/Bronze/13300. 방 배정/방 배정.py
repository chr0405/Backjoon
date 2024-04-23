N, K = map(int, input().split())
studentList = [[0] * 6 for _ in range(2)]
count = 0

for student in range(N):
    S, Y = map(int, input().split())
    studentList[S][Y - 1] += 1

for sex in studentList:
    for year in sex:
        count += year // K
        if year % K:
            count += 1

print(count)
