N_list = [i for i in range(1, 31)]

for i in range(28) :
    n = int(input())
    N_list.remove(n)

print(min(N_list))
print(max(N_list))
