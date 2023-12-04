N = int(input())

count = 1 # 벌집의 수. 1개부터 시작
jumping = 1 # 이동해야 하는 방의 수. 시작점도 count하니까 1
while N > count :
    count += 6 * jumping
    jumping += 1
print(jumping)