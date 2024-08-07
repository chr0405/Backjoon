import sys

def backtrack(N, M, start, path):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return
    
    for i in range(start, N + 1):
        path.append(i)
        backtrack(N, M, i, path)
        path.pop()

def solve():
    N, M = map(int, sys.stdin.readline().split())
    backtrack(N, M, 1, [])

solve()