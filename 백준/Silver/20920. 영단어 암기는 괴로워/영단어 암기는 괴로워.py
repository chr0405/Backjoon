import sys
from collections import Counter

input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
words = [word for word in data[1:] if len(word) >= m]

word_count = Counter(words)

sorted_words = sorted(word_count.keys(), key=lambda x: (-word_count[x], -len(x), x))

print("\n".join(sorted_words))
