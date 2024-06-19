import sys

n = int(sys.stdin.readline().strip())

def hanoi(a, b, n):

    if n == 1:
        print(f"{a} {b}")
        return

    c = 6 - a - b
    hanoi(a, c, n-1)
    print(f"{a} {b}")
    hanoi(c, b, n - 1)

print(2**n - 1)
hanoi(1, 3, n)