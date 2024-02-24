import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Count = 0
N_Set = set(input() for i in range(N))
MN_List = list()

for j in range(M):
    M_member = input()
    if M_member in N_Set:
        MN_List.append(M_member.strip())
        Count += 1

MN_List.sort()
print(Count)
print(*MN_List, sep='\n')

