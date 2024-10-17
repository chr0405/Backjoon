import sys
input = sys.stdin.readline

N = int(input().strip())  # 도시의 수
array1 = list(map(int, input().split()))  # 도시 간 거리
array2 = list(map(int, input().split()))  # 리터당 가격

totalValue = 0
minPrice = array2[0] 

for index in range(N-1):
    if array2[index] < minPrice:
        minPrice = array2[index]
    totalValue += minPrice * array1[index]

print(totalValue)