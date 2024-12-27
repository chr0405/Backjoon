import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
results = []
idx = 1

for _ in range(t):
    m, n, x, y = map(int, data[idx:idx+4])
    idx += 4
    found = False
    while x <= m * n:
        if (x - y) % n == 0:
            results.append(x)
            found = True
            break
        x += m
    if not found:
        results.append(-1)

sys.stdout.write("\n".join(map(str, results)) + "\n")
