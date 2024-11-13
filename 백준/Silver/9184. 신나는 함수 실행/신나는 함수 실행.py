import sys
input = sys.stdin.readline

wList = [[[0] * 21 for _ in range(21)] for _ in range(21)]

for a in range(21):
    for b in range(21):
        for c in range(21):
            if a <= 0 or b <= 0 or c <= 0:
                wList[a][b][c] = 1
            elif (a < b) and (b < c):
                wList[a][b][c] = wList[a][b][c-1] + wList[a][b-1][c-1] - wList[a][b-1][c-1]
            else:
                wList[a][b][c] = wList[a-1][b][c] + wList[a-1][b-1][c] + wList[a-1][b][c-1] - wList[a-1][b-1][c-1]

while True:

    a, b, c = map(int, input().split())
    answer = 0

    if a == -1 and b == -1 and c == -1:
        break
    elif a <= 0 or b <= 0 or c <= 0:
        answer = 1
    elif a > 20 or b > 20 or c > 20:
        answer = wList[20][20][20]
    else:
        answer = wList[a][b][c]

    print(f'w({a}, {b}, {c}) = {answer}')