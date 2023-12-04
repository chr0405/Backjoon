def DAC(size, x, y):
    Mid = size // 2
    if size == 1: return N_list[x][y]
    if size == 2:
        Answer = [N_list[x][y], N_list[x + 1][y], N_list[x][y + 1], N_list[x + 1][y + 1]]
        Answer.sort()
        return Answer[1]
    lt = DAC(Mid, x, y)
    rt = DAC(Mid, x + Mid, y)
    lb = DAC(Mid, x, y + Mid)
    rb = DAC(Mid, x + Mid, y + Mid)
    Answer = [lt, rt, lb, rb]
    Answer.sort()
    return Answer[1]
    
    

N = int(input())
N_list = []
for i in range(N):
    Tmp = list(map(int, input().split()))
    N_list.append(Tmp)
print(DAC(N, 0, 0))