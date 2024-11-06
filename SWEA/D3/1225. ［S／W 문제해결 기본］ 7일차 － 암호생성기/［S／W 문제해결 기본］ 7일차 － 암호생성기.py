from collections import deque

for _ in range(10):
    tc = int(input().strip())
    numList = deque(map(int, input().split()))
    sub = 1
    
    while True:
        num = numList.popleft()
        num -= sub
        
        if num < 0:
            num = 0
        
        numList.append(num)
        
        if numList[-1] == 0:  
            break
        
        if sub < 5:
            sub += 1
        else: sub = 1
        
    answer = ' '.join(map(str, numList))
    print(f'#{tc} {answer}')
