T = int(input())
for t in range(1, T + 1):
    P, Q = map(float, input().split())
    p1 = (1 - P) * Q
    p2 = P * (1 - Q) * Q
    result = "YES" if p1 < p2 else "NO"
    print(f"#{t} {result}")
