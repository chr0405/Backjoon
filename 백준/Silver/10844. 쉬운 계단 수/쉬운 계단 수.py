MOD = 1000000000

def easy_staircase_numbers(n):
    dp = [[0] * 10 for _ in range(n + 1)]

    for i in range(1, 10):
        dp[1][i] = 1

    for i in range(2, n + 1):
        for j in range(10):
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]
            if j < 9:
                dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= MOD

    return sum(dp[n]) % MOD

n = int(input())
print(easy_staircase_numbers(n))