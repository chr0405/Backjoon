S = input()
Arr = [0]*26

for _ in S:
    Arr[ord(_)-97] += 1

for _ in Arr:
    print(_, end=' ')