import sys
input = sys.stdin.readline

N = int(input().strip())
peopelList = list(map(int, input().split()))

peopelList.sort()
t = 0
sum = 0

for i in peopelList:
    sum += (t + i)
    t += i

print(sum)