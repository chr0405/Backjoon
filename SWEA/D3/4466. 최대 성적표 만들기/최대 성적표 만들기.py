T = int(input())
for t in range(1, T + 1):
    n, k = map(int, input().split())
    scores = sorted(map(int, input().split()), reverse=True)
    print(f"#{t} {sum(scores[:k])}")
