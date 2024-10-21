for i in range(1, 10 + 1):
    num = int(input())
    
    N, M = map(int, input().split())
    
    answer = N**M
    
    print(f'#{num} {answer}')