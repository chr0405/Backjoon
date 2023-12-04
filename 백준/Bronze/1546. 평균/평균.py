N = int(input())
N_list = list(map(int, input().split()))
M = max(N_list)

Edit_list = []
for _ in N_list :
    Edit_list.append(_ / M * 100)

avg = sum(Edit_list)/N
print(avg)