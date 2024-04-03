import math
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

# nRange = 1000001
# nList = [1] * nRange
# for i in range(1, nRange):
#     if i == 1:
#         continue
#     for j in range(2, int(math.sqrt(i))+1):
#         if i % j == 0:
#             nList[i] = 0
#             break

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     count = 0
#     for i in range(2, int(N/2) + 1):
#         if nList[i] and nList[N-i]:
#             count += 1
#     print(count)

nRange = 1000001
prime = []
check = [1, 1] + [0] * 999999

for i in range(2, nRange):
    if check[i] == 0:
        prime.append(i)
        for j in range(2*i, nRange, i):
            check[j] = 1

T = int(input())

for _ in range(T):
    count = 0
    N = int(input())
    for i in prime:
        if i >= N:
            break
        if not check[N - i] and i <= N-i:
            count += 1
    print(count)