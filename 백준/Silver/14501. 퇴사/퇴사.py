import sys
input = sys.stdin.readline

def max_profit(N, consultations):
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        T, P = consultations[i - 1]
        
        if i + T - 1 <= N:
            dp[i + T - 1] = max(dp[i + T - 1], dp[i - 1] + P)
        
        dp[i] = max(dp[i], dp[i - 1])

    return max(dp)

N = int(input())
consultations = [tuple(map(int, input().split())) for _ in range(N)]

result = max_profit(N, consultations)
print(result)