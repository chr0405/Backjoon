import sys

def Func(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = Func(n - 1) + Func(n - 2)
        return result

n = int(sys.stdin.readline())
answer = Func(n)
print(answer)