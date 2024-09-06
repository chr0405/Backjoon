import sys

input = sys.stdin.readline

s = input().strip()
suffixes = [s[i:] for i in range(len(s))]

suffixes.sort()

for suffix in suffixes:
    print(suffix)