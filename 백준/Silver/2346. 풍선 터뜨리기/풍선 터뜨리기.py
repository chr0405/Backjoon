from collections import deque

n = int(input())
balloons = list(map(int, input().split()))

balloons = deque((i + 1, num) for i, num in enumerate(balloons))

result = []

while balloons:
    index, num = balloons.popleft()
    result.append(index)
    
    if balloons:
        if num > 0:
            balloons.rotate(-(num - 1))
        else:
            balloons.rotate(-num)

print(' '.join(map(str, result)))