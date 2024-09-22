import sys
input = sys.stdin.readline

n = int(input().strip()) 
logs = {}

for _ in range(n):
    name, status = input().split()

    if status == "enter":
        logs[name] = True 
    else:
        logs.pop(name)

for name in sorted(logs.keys(), reverse=True):
    print(name)