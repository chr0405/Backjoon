import sys

N, r, c = map(int, sys.stdin.readline().split())

def recursion(N, r, c):
    if N == 0:
        return 0
    
    half = 2 ** (N - 1)
    
    if r < half and c < half:
        return recursion(N - 1, r, c)
    elif r < half and c >= half:
        return half**2 + recursion(N - 1, r, c - half)
    elif r >= half and c < half:
        return half**2 * 2 + recursion(N - 1, r - half, c)
    elif r >= half and c >= half:
        return half**2 * 3 + recursion(N - 1, r - half, c - half)

print(recursion(N, r, c))