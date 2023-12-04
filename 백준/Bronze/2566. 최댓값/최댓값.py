A_list = []
A_list = [list(map(int, input().split())) for _ in range(9)]
MaxValue = -1
MaxRow = 0
MaxCol = 0

for i in range(9) :
    for j in range(9) :
        if A_list[i][j] > MaxValue :
            MaxValue = A_list[i][j]
            MaxRow = i + 1
            MaxCol = j + 1

print(MaxValue)
print(MaxRow, MaxCol, end = " ")