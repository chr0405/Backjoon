n = int(input())

divisors = list(map(int, input().split()))

min_divisor = min(divisors)
max_divisor = max(divisors)
N = min_divisor * max_divisor

print(N)
