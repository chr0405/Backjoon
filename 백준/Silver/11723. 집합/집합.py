import sys
input = sys.stdin.readline

m = int(input())
S = 0

for _ in range(m):
    command = input().split()
    if command[0] == "add":
        S |= (1 << int(command[1]))
    elif command[0] == "remove":
        S &= ~(1 << int(command[1]))
    elif command[0] == "check":
        print(1 if S & (1 << int(command[1])) else 0)
    elif command[0] == "toggle":
        S ^= (1 << int(command[1]))
    elif command[0] == "all":
        S = (1 << 21) - 1
    elif command[0] == "empty":
        S = 0
