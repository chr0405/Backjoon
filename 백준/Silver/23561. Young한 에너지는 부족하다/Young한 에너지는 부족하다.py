n = int(input())
ages = list(map(int, input().split()))
ages.sort()
energies = [ages[n + i] for i in range(n)]
print(max(energies) - min(energies))
