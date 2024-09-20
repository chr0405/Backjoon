import sys

# 동전의 종류(개수는 제한 없음), 금액
N, K = map(int, sys.stdin.readline().split())
coins = []

for _ in range(N):
    coins.append(int(sys.stdin.readline().strip()))

# 큰 순으로
coins.sort(reverse=True)

count = 0
for coin in coins:
    if K == 0:
        break

    # 몫이 0이면(= 동전의 가치가 금액보다 크면) count가 변경되지 않음
    count += K // coin
    # 동전의 가치가 금액보다 크면 K가 변경되지 않음
    K %= coin

print(count)