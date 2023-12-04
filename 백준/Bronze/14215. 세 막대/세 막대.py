N_list = list(map(int, input().split()))

# if a == b == c : print(sum(N_list))
if len(set(N_list)) == 1 : print(sum(N_list))
elif max(N_list) * 2 < sum(N_list) : print(sum(N_list))
else: print((sum(N_list) - max(N_list)) * 2 - 1)