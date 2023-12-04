T = int(input())

for _ in range(T) :
    C = int(input())
    if (C // 25 >= 0) : print (C // 25, end = " "); C -= (C // 25) * 25
    else : print(0, end = " ")
    if (C // 10 >= 0) : print (C // 10, end = " "); C -= (C // 10) * 10
    else : print(0, end = " ")
    if (C // 5 >= 0) : print (C // 5, end = " "); C -= (C // 5) * 5
    else : print(0, end = " ")
    if (C // 1 >= 0) : print (C // 1, end = " "); C -= (C // 1) * 1
    else : print(0)
    print()