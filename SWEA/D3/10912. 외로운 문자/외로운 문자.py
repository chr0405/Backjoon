T = int(input())  # 테스트 케이스의 수
for t in range(1, T + 1):
    string = input()
    result = []
    for char in sorted(set(string)):
        if string.count(char) % 2 != 0:
            result.append(char)
    print(f"#{t} {''.join(result) if result else 'Good'}")
