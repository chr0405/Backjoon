import sys

N = int(sys.stdin.readline().split()[0])
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [0, 0, 0]

def check_paper(paper, x, y, size):
    value = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != value:
                return False
    return True

def count_paper(paper, x, y, size, result):
    if check_paper(paper, x, y, size):
        result[paper[x][y] + 1] += 1
    else:
        offset = size // 3
        for i in range(3):
            for j in range(3):
                count_paper(paper, x + i * offset, y + j * offset, offset, result)

count_paper(paper, 0, 0, N, result)

for count in result:
    print(count)