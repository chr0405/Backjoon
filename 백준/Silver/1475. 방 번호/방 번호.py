import math

N = str(input())
Count = 1
Arr = []

for num in range(10):
    Arr.append(N.count(str(num)))

term = Arr[6] + Arr[9]

if(term % 2 == 0):
    Arr[6] = math.floor(term / 2)
else:
    Arr[6] = math.floor(term / 2) + 1
Arr[9] = 0

print(max(Arr))