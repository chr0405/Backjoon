import sys

N = int(sys.stdin.readline().strip())
N_list = []

for _ in range(N):
    i = int(sys.stdin.readline().strip())
    N_list.append(i)

N_list.sort()

for i in N_list:
    print(i)