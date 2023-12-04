X_list = []
Y_list = []
for i in range(3):
    X, Y = map(int, input().split())
    X_list.append(X)
    Y_list.append(Y)
for i in range(3):
    if X_list.count(X_list[i]) == 1:
        X = X_list[i]
    if Y_list.count(Y_list[i]) == 1:
        Y = Y_list[i]
print(X, Y)