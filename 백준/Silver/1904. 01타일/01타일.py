import sys
input = sys.stdin.readline

N = int(input().strip())

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    back2 = 1
    back1 = 2

    for i in range(3, N + 1):
        answer = (back1 + back2) % 15746  # 각 연산마다 모듈러 연산을 적용
        back2 = back1
        back1 = answer

    print(answer)
