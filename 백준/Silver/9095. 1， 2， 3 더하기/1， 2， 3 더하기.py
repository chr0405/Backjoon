import sys

T = int(sys.stdin.readline().strip()) # test case 갯수
dq = [0] * 12

dq[1] = 1
dq[2] = 2
dq[3] = 4

for i in range(4, 12):
    dq[i] = dq[i-1]+dq[i-2]+dq[i-3]

for _ in range(T):
    n = int(sys.stdin.readline().strip())
    print(dq[n])