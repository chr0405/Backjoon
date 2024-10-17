import sys
input = sys.stdin.readline

N = int(input().strip())

array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

minValue = min(array2[:-1])
totalValue = 0

for index in range(N-1):
    if array2[index] == minValue:
        totalValue += minValue * sum(array1[index:])
        break
    else:
        totalValue += array1[index] * array2[index]
    
print(totalValue)