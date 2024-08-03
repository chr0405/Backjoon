import sys

def count_subsequences(arr, N, S):
    def backtrack(index, current_sum):
        nonlocal count
        if index == N:
            if current_sum == S:
                count += 1
            return
        
        backtrack(index + 1, current_sum + arr[index])
        backtrack(index + 1, current_sum)

    count = 0
    backtrack(0, 0)
    return count

N, S = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

result = count_subsequences(arr, N, S)

if S == 0:
    result -= 1

print(result)