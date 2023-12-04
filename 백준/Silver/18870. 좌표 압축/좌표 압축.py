N = int(input())
N_list = list(map(int, input().split()))

New_list = sorted(list(set(N_list)))
dic = {New_list[i] : i for i in range(len(New_list))}
for i in N_list:
    print(dic[i], end = " ")