T = int(input())
i = 0
while(i < T) :
    i += 1
    a, b = map(int, input().split())
    print("Case #", i, ":", sep = "", end = " ")
    print(a, "+", b, "=", a + b)