import sys

N = int(sys.stdin.readline().strip())
alphaDict = {}

for _ in range(N):
  word = sys.stdin.readline().strip()
  alphaDict[word] = len(word)

def sortFunc(word) :
  wordKey, wordLen = word
  return wordLen, wordKey

alphaDict = sorted(alphaDict.items(), key = sortFunc)

for wordKey, wordLen in alphaDict:
  print(wordKey)