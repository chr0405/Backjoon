import sys

N = int(sys.stdin.readline().strip())
cardDictionary = {}

for _ in range(N):
    card = int(sys.stdin.readline().strip())
    if card in cardDictionary:
        cardDictionary[card] += 1
    else:
        cardDictionary[card] = 1

max = 0
most = None

for card, count in cardDictionary.items():
    if count > max or (count == max and card < most): # 갯수가 max 값보다 크거나, 갯수가 max 값과 같으며 카드 값이 most보다 작을 때
        max = count
        most = card

print(most)