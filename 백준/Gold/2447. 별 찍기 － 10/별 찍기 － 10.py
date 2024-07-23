import sys

N = int(sys.stdin.readline().strip())

def recursion(n):

    if n == 1:
        startArray1 = ["*"]
        return startArray1

    startArray = recursion(n//3)
    Array = []

    for i in range(n):
        if i // (n // 3) == 1:
            Array.append(startArray[i % (n // 3)] + " " * (n // 3) + startArray[i % (n // 3)])
        else:
            Array.append(startArray[i % (n // 3)] * 3)
    
    return Array


last_result = recursion(N)

for line in last_result:
    print(line)