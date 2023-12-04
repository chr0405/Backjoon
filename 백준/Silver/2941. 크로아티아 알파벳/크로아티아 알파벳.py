N_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
N = input()

for _ in N_list :
    N = N.replace(_ , 'a')
print(len(N))