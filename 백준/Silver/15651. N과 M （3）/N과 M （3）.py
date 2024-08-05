import sys

def backtrack(N, M, sequence):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return

    for i in range(1, N + 1):
        sequence.append(i)
        backtrack(N, M, sequence)
        sequence.pop()

N, M = map(int, sys.stdin.readline().strip().split())

backtrack(N, M, [])