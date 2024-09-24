import sys
input = sys.stdin.readline

N, K = map(int, input().split())
sequence = list(map(int, input().split()))

seen = set()
unique_numbers = []
for num in sequence:
    if num not in seen:
        seen.add(num)
        unique_numbers.append(num)

count_dict = {}
for num in sequence:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

sorted_numbers = sorted(sequence, key=lambda x: (-count_dict[x], unique_numbers.index(x)))

print(" ".join(map(str, sorted_numbers)))