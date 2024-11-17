import sys
input = sys.stdin.read
data = input().splitlines()

s = data[0]
q = int(data[1])
prefix = [[0] * 26 for _ in range(len(s) + 1)]

for i in range(len(s)):
    for j in range(26):
        prefix[i + 1][j] = prefix[i][j]
    prefix[i + 1][ord(s[i]) - ord('a')] += 1

result = []
for i in range(2, 2 + q):
    char, l, r = data[i].split()
    l, r = int(l), int(r)
    idx = ord(char) - ord('a')
    result.append(prefix[r + 1][idx] - prefix[l][idx])

print('\n'.join(map(str, result)))