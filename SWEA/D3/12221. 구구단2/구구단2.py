T = int(input().strip())

for i in range(1, T+1):
    A, B = map(int, input().split())
    
    if A >= 10 or B >= 10:
        print(f'#{i} {-1}')
        continue
    else: print(f'#{i} {A * B}')