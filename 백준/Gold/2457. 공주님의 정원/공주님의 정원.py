import sys
input = sys.stdin.readline

def changeDate(month, day):
    return month * 100 + day

n = int(input().strip())
flowers = []

for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    flowers.append((changeDate(sm, sd), changeDate(em, ed)))

flowers.sort()

start = changeDate(3, 1)
last_end = changeDate(11, 30)

count = 0
index = 0
newStart = start

while start <= last_end:
    found = False

    while index < n and flowers[index][0] <= start:
        newStart = max(newStart, flowers[index][1])
        index += 1
        found = True

    if not found:
        print(0)
        break

    count += 1
    start = newStart

if found:
    print(count)
