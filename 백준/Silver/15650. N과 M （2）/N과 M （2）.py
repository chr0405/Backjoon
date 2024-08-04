import sys
input = sys.stdin.readline

def backtrack(N, M, start, sequence):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return

    for i in range(start, N + 1):
        sequence.append(i)
        backtrack(N, M, i + 1, sequence)
        sequence.pop()

N, M = map(int, input().strip().split())

backtrack(N, M, 1, [])