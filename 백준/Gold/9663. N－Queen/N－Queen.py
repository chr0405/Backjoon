import sys
N = int(sys.stdin.readline().strip())

def backtrack(row):
    global count
    if row == N:
        count += 1
        return
    
    for col in range(N):
        if not cols[col] and not diag1[row + col] and not diag2[row - col + N - 1]:
            cols[col] = diag1[row + col] = diag2[row - col + N - 1] = True
            backtrack(row + 1)
            cols[col] = diag1[row + col] = diag2[row - col + N - 1] = False

cols = [False] * N
diag1 = [False] * (2 * N - 1)
diag2 = [False] * (2 * N - 1)
count = 0

backtrack(0)

print(count)