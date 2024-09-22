import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokedex_num_to_name = {} 
pokedex_name_to_num = {}  

for i in range(1, N + 1):
    name = input().strip()
    pokedex_num_to_name[i] = name
    pokedex_name_to_num[name] = i

for _ in range(M):
    query = input().strip()
    if query.isdigit():
        print(pokedex_num_to_name[int(query)]) 
    else:
        print(pokedex_name_to_num[query])