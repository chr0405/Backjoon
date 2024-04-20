A = int(input())
B = int(input())
C = int(input())

Arr = [0] * 10

ABC = str(A*B*C)

for _ in ABC:
    Arr[ord(_) - 48] += 1

for _ in Arr:
    print(_)