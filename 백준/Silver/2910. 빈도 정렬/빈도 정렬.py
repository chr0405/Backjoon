from collections import Counter
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
sequence = list(map(int, input().split()))

freq = Counter(sequence)

order = {}
for index, num in enumerate(sequence):
    if num not in order:
        order[num] = index

sorted_numbers = sorted(sequence, key=lambda x: (-freq[x], order[x]))

print(" ".join(map(str, sorted_numbers)))