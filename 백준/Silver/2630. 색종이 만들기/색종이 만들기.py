import sys

N = int(sys.stdin.readline().strip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = [0, 0]

def check_paper(paper, x, y, size):
    color = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                return False
    return True

def count_paper(paper, x, y, size):
    if check_paper(paper, x, y, size):
        result[paper[x][y]] += 1
    else:
        half = size // 2
        count_paper(paper, x, y, half)
        count_paper(paper, x, y + half, half)
        count_paper(paper, x + half, y, half)
        count_paper(paper, x + half, y + half, half)

count_paper(paper, 0, 0, N)

print(result[0])
print(result[1])