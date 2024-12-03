T = int(input())
for t in range(1, T + 1):
    sides = list(map(int, input().split()))
    for side in sides:
        if sides.count(side) % 2 == 1:
            print(f"#{t} {side}")
            break
