N = int(input())
N_list = []

for _ in range(N):
    i = int(input())
    N_list.append(i)

N_list.sort()

for i in N_list:
    print(i)