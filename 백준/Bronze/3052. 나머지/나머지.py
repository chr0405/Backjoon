N_list = []

for i in range(10) :
    N = int(input())
    N_list.append(N % 42)

N_list = set(N_list) # set 함수를 통해 중복 제거 가능
print(len(N_list)) # len은 길이를 출력해주는 함수