n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left, right = 0, n - 1
closest_sum = float('inf')
answer = (0, 0)

while left < right:
    current_sum = arr[left] + arr[right]

    if abs(current_sum) < abs(closest_sum):
        closest_sum = current_sum
        answer = (arr[left], arr[right])

    if current_sum < 0:
        left += 1
    elif current_sum > 0:
        right -= 1
    else:
        break

print(answer[0], answer[1])
