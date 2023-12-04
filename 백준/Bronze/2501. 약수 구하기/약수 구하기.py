N, K = map(int, input().split())
N_list = []

for i in range(1, N+1):
    if N % i == 0 : N_list.append(i)

if K > len(N_list) : print(0)
else : print(N_list[K-1])