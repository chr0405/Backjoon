import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
keywords = set(data[1:n+1])
result = []

for i in range(n+1, n+1+m):
    removed_keywords = set(data[i].split(","))
    keywords -= removed_keywords
    result.append(len(keywords))

print("\n".join(map(str, result)))
