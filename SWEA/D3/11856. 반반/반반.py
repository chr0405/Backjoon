T = int(input())
for TC in range(1, T + 1):
    S = input()
    counts = [0] * 26
    result = "Yes"

    for char in S:
        idx = ord(char) - 65
        counts[idx] += 1
        if counts[idx] > 2:
            result = "No"
            break

    if counts.count(2) != 2:
        result = "No"

    print(f"#{TC} {result}")
