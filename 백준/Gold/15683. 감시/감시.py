from collections import deque
import sys
input = sys.stdin.readline

# 사무실의 세로(N), 가로(M)
N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]

# 남, 동, 북, 서 방향을 가리킴 (남쪽을 시작으로 반시계방향으로 돌아가는 순서로 되어 있음)
dy = [1, 0, -1, 0] # y축
dx = [0, 1, 0, -1] # x축

# 감시해야하는 모든 방향 (각각의 cctv별로 감시할 수 있는 방향)
direction = {
    1: [[0], [1], [2], [3]],            # 1번cctv 방향:0, 1, 2, 3, --> 4가지
    2: [[0, 2], [1, 3]],                    # 2번cctv 방향:(0, 2), (1, 3) --> 2가지
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],    # 3번cctv 방향:(0, 1), (1, 2), (2, 3), (3, 0) --> 4가지
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],    # 4번cctv 방향 --> 4가지
    5: [[0, 1, 2, 3]]                      # 5번cctv 방향 --> 1가지
}

# cctv좌표들(cctv 번호, 행, 렬), 빈칸(0)의 개수 초기화
# 0의 개수 초기화
cctv = deque()
answer = 0

for i in range(N):
    for j in range(M):
        # 벽이 아니고 빈칸이 아니면
        if space[i][j] != 6 and space[i][j] != 0:
            cctv.append((space[i][j], i, j))  # cctv 번호, cctv 좌표 저장
        # cctv가 없는 경우 빈칸의 갯수를 센다
        if space[i][j] == 0:
            answer += 1


def move(y, x, direc, space_copy): # 해당 cctv의 행, 렬, 해당 cctv의 감시해야 하는 방향 (for문을 돌며 하나씩), 현재 사무실의 상태
    # 각각의 방향에 대해서 전부 이동시켜줌
    for d in direc:
        # ex. direc = [0, 2]
        # d는 for문을 돌며 차례대로 0, 2

        ny, nx = y, x # 해당 cctv의 행, 렬
        
        while True:
            nx += dx[d]
            ny += dy[d]
            # 범위를 벗어났거나 벽을 만났다면 
            if not (0 <= ny < N and 0 <= nx < M) or space_copy[ny][nx] == 6:
                break # while문을 벗어난다
            # 빈칸이 아니면 (cctv나 앞전에 # 체크한 영역일 경우)
            if space_copy[ny][nx] != 0:
                continue # 건너뛰고 다음을 진행
            # 빈칸일 경우 # 체크
            space_copy[ny][nx] = '#'


def dfs(level, space):
    space_copy = [[j for j in space[i]] for i in range(N)]
    # level이 커지기 전 (깊이가 커지기 전) 상태의 배열을 저장함
   
    if level == len(cctv): # 모든 cctv를 확인했다면
        # 사각지대를 구한다
        global answer
        cnt = 0
        for i in space_copy:
            cnt += i.count(0) # 빈 공간의 개수를 센다
        answer = min(answer, cnt) # 처음 센 빈 공간의 개수를 시작으로 최솟값을 비교하며 값을 구함
        return			# 전 상태로 돌아감
    
    number, y, x  = cctv[level] # cctv좌표들(cctv 번호, 행, 렬)
    
    # number번째 cctv에 대해 가능한 모든 방향을 순차적으로 고려 
    for d in direction[number]: # direction : cctv 별로 감시해야 하는 모든 방향을 담고 있는 딕셔너리
        # ex. direction[2] = [[0, 2], [1, 3]]
        # d는 for문을 돌며 차례대로 [0, 2], [1, 3]
        move(y, x, d, space_copy) # 행, 렬, 해당 cctv의 감시해야 하는 방향 (for문을 돌며 하나씩), 현재 사무실의 상태
        dfs(level+1, space_copy)   # level+1 번째 cctv를 고려
        space_copy = [[j for j in space[i]] for i in range(N)]
        # level이 커지기 전 (깊이가 커지기 전, dfs로 재귀하기 전) 상태의 배열로 복구

dfs(0, space) # start값과 입력받은 배열
print(answer)