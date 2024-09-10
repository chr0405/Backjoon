import sys

def count_ways(n):
    dp = [0] * (12)
    
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    for i in range(4, 12):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    print(count_ways(n))