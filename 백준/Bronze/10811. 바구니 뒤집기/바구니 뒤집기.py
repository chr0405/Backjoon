N, M = map(int, input().split())
N_list = [n for n in range(1, N + 1)] #range 범위 다름

for _ in range(M):
    i, j = map(int, input().split())
    N_list = N_list[:i-1] + N_list[i-1:j][::-1] + N_list[j:]

for i in N_list :
    print(i, end = ' ')