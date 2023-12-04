X = int(input())
N = int(input())
i = 0
x = 0
while(i < N) :
    i += 1
    a, b = map(int, input().split())
    x += a * b

if((X - x) == 0) :
    print("Yes")
else : print("No")