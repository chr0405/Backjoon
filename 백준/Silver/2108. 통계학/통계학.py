import sys
from collections import Counter

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]
numbers.sort()

mean = round(sum(numbers) / n)

median = numbers[n // 2]

counter = Counter(numbers)
modes = counter.most_common() 
if len(modes) > 1 and modes[0][1] == modes[1][1]:
    mode = modes[1][0]
else:
    mode = modes[0][0]

range_value = numbers[-1] - numbers[0]

print(mean)
print(median)
print(mode)
print(range_value)
