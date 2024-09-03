import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])

numbers = [int(num[::-1]) for num in data[1:]]

numbers.sort()

for num in numbers:
    print(num)