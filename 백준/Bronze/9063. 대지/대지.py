N = int(input())
x_list = []
y_list = []

for _ in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_lenth = (max(x_list) - min(x_list))
y_lenth = (max(y_list) - min(y_list))

print(x_lenth * y_lenth)