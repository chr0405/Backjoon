import sys

N = int(sys.stdin.readline().strip())
paper = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

def check_paper(paper, x, y, size):
    color = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                return False
    return True

def quad_tree(paper, x, y, size):
    if check_paper(paper, x, y, size):
        return str(paper[x][y])
    else:
        half = size // 2
        top_left = quad_tree(paper, x, y, half)
        top_right = quad_tree(paper, x, y + half, half)
        bottom_left = quad_tree(paper, x + half, y, half)
        bottom_right = quad_tree(paper, x + half, y + half, half)
        return f"({top_left}{top_right}{bottom_left}{bottom_right})"

result = quad_tree(paper, 0, 0, N)
print(result)