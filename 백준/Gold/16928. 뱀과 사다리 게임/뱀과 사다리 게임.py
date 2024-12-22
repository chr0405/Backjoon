from collections import deque

n, m = map(int, input().split())
board = {i: i for i in range(1, 101)}

for _ in range(n + m):
    x, y = map(int, input().split())
    board[x] = y

visited = [False] * 101
queue = deque([(1, 0)])

while queue:
    current, moves = queue.popleft()
    if current == 100:
        print(moves)
        break

    for dice in range(1, 7):
        next_pos = current + dice
        if next_pos <= 100 and not visited[next_pos]:
            visited[next_pos] = True
            queue.append((board[next_pos], moves + 1))
