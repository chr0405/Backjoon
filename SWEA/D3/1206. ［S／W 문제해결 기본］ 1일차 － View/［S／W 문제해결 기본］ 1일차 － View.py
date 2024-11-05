for i in range(1, 11):
    buildingCount = int(input().strip())
    buildingList = list(map(int, input().split()))
    count = 0
    
    for j in range(2, len(buildingList) - 2):
        if buildingList[j-2] < buildingList[j] and buildingList[j-1] < buildingList[j] and\
        	buildingList[j+1] < buildingList[j] and buildingList[j+2] < buildingList[j]:
                maxHeight = max(buildingList[j-2], buildingList[j-1], buildingList[j+1], buildingList[j+2])
                count += buildingList[j] - maxHeight
        
    print(f'#{i} {count}')