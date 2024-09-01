import sys
from collections import Counter

n = int(sys.stdin.readline())
cards = []

for _ in range(n):
    cards.append(int(sys.stdin.readline()))

counter = Counter(cards)

max_frequency = max(counter.values())

most_frequent_cards = [card for card, freq in counter.items() if freq == max_frequency]

print(min(most_frequent_cards))