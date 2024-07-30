from collections import deque
import sys

F, S, G, U, D = map(int, sys.stdin.readline().split())

Floors = [-1] * (F + 1)

Floors[S] = 0
queue = deque([S])

while queue:
    now = queue.popleft()

    for spot in [U, (D * -1)]:
        move = now + spot

        if 0 < move <= F and Floors[move] == -1:
            Floors[move] = Floors[now] + 1
            queue.append(move)

        if move == G:
            break

if Floors[G] == -1:
    print("use the stairs")
else: print(Floors[G])