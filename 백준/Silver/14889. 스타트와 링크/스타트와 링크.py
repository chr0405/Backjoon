n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
min_diff = float('inf')

def dfs(depth, idx):
    global min_diff
    if depth == n // 2:
        team_start, team_link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    team_start += s[i][j]
                elif not visited[i] and not visited[j]:
                    team_link += s[i][j]
        min_diff = min(min_diff, abs(team_start - team_link))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

dfs(0, 0)
print(min_diff)
