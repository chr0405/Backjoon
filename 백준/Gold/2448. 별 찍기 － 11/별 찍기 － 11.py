import sys

N = int(sys.stdin.readline().strip())

def recursion(n):

    if n == 3:
        startArray1 = ["  *  ", " * * ", "*****"]
        return startArray1

    startArray = recursion(n // 2)
    Array = []

    for i in range(n // 2):
        Array.append(" " * (n // 2) + startArray[i] + " " * (n // 2))
    for i in range(n // 2):
        Array.append(startArray[i] + " " + startArray[i])

    return Array


last_result = recursion(N)

for line in last_result:
    print(line)