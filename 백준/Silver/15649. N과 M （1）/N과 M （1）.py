import sys

def backtrack(N, M, sequence, used):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return

    for i in range(1, N + 1):
        if not used[i]:
            used[i] = True
            sequence.append(i)
            backtrack(N, M, sequence, used)
            sequence.pop()
            used[i] = False

N, M = map(int, sys.stdin.readline().split())
used = [False] * (N + 1)

backtrack(N, M, [], used)