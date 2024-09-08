import sys
from bisect import bisect_right

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    
    B.sort()
    count = 0
    
    for a in A:
        count += bisect_right(B, a - 1)
    
    print(count)