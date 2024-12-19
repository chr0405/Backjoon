n, m = map(int, input().split())
nums = list(map(int, input().split()))
prefix = [0] * n
count = [0] * m
prefix[0] = nums[0] % m
count[prefix[0]] += 1
for i in range(1, n):
    prefix[i] = (prefix[i - 1] + nums[i]) % m
    count[prefix[i]] += 1
result = count[0]
for c in count:
    result += c * (c - 1) // 2
print(result)
