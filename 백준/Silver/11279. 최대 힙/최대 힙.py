import sys
import heapq

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
max_heap = []
result = []

for i in range(1, n + 1):
    x = int(data[i])
    if x == 0:
        if max_heap:
            result.append(-heapq.heappop(max_heap))
        else:
            result.append(0)
    else:
        heapq.heappush(max_heap, -x)

print("\n".join(map(str, result)))
