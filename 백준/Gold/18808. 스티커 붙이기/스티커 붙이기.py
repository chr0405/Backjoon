import sys

def rotate_90(sticker):
    return list(zip(*sticker[::-1]))

def can_attach(notebook, sticker, x, y):
    rows, cols = len(sticker), len(sticker[0])
    for i in range(rows):
        for j in range(cols):
            if sticker[i][j] == 1:
                if notebook[x + i][y + j] == 1:
                    return False
    return True

def attach(notebook, sticker, x, y):
    rows, cols = len(sticker), len(sticker[0])
    for i in range(rows):
        for j in range(cols):
            if sticker[i][j] == 1:
                notebook[x + i][y + j] = 1

def solve():
    n, m, k = map(int, input().split())
    
    notebook = [[0] * m for _ in range(n)]
    for _ in range(k):
        r, c = map(int, input().split())
        sticker = [list(map(int, input().split())) for _ in range(r)]
        
        attached = False
        for _ in range(4):
            if attached:
                break
            for i in range(n - len(sticker) + 1):
                if attached:
                    break
                for j in range(m - len(sticker[0]) + 1):
                    if can_attach(notebook, sticker, i, j):
                        attach(notebook, sticker, i, j)
                        attached = True
                        break
            if not attached:
                sticker = rotate_90(sticker)
    
    print(sum(sum(row) for row in notebook))

solve()