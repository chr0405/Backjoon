import sys

def Func(N):
    if N == 0:
        return 1
    else:
        result = N * Func(N - 1)
        return result

N = int(sys.stdin.readline())
answer = Func(N)
print(answer)