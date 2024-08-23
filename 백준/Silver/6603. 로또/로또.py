import sys
from itertools import combinations

while True:
    array = list(map(int, sys.stdin.readline().split()))
    
    if array[0] == 0:
        break
    
    k = array[0]
    S = array[1:]
    
    for comb in combinations(S, 6):
        print(" ".join(map(str, comb)))
    
    print()