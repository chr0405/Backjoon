def dfs(index, current_result, add, sub, mul, div):
    global max_result, min_result

    if index == n:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return

    if add > 0:
        dfs(index + 1, current_result + numbers[index], add - 1, sub, mul, div)
    if sub > 0:
        dfs(index + 1, current_result - numbers[index], add, sub - 1, mul, div)
    if mul > 0:
        dfs(index + 1, current_result * numbers[index], add, sub, mul - 1, div)
    if div > 0:
        dfs(index + 1, int(current_result / numbers[index]), add, sub, mul, div - 1)


n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = -float('inf')
min_result = float('inf')

dfs(1, numbers[0], add, sub, mul, div)

print(max_result)
print(min_result)
