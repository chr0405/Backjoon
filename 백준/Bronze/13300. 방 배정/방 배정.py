import sys
input = sys.stdin.readline

N, K = map(int,input().split())
students = [[0,0] for _ in range(6)] # [여,남] * 6
res = 0

for _ in range(N):
    S, Y = map(int,input().split())
    students[Y-1][S]+=1

for grade in students:
    for num in grade:
        res+=num//K
        if num % K:
            res+=1
    
print(res)