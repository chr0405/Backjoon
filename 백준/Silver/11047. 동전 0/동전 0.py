N, K = map(int, input().split())
coinList = []
count = 0

for _ in range(N):
    coin = int(input().strip())
    coinList.append(coin)
    
coinList.sort(reverse=True)

for coin in coinList:
    quot = K // coin
    if quot >= 1:
        count += quot
        K %= coin

print(count)