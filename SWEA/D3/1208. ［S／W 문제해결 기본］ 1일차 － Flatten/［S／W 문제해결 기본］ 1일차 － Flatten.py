for i in range(1, 11):
    dump = int(input().strip())
    boxList = list(map(int, input().split()))
    
    while dump > 0:
        boxList.sort()  
        if boxList[-1] - boxList[0] <= 1:
            break
        boxList[-1] -= 1
        boxList[0] += 1
        dump -= 1
        
    boxList.sort() 
    answer = boxList[-1] - boxList[0]
    print(f'#{i} {answer}')
