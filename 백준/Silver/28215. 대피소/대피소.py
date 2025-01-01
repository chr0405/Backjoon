from itertools import combinations

N, K = map(int, input().split())
houses = [tuple(map(int, input().split())) for _ in range(N)]

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

min_max_distance = float('inf')

for shelters in combinations(houses, K):
    max_distance = 0
    for house in houses:
        min_distance = min(manhattan_distance(house, shelter) for shelter in shelters)
        max_distance = max(max_distance, min_distance)
    min_max_distance = min(min_max_distance, max_distance)

print(min_max_distance)
