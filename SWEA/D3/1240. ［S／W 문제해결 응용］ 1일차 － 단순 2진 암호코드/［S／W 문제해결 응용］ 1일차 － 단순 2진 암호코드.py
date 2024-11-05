T = int(input().strip())

scanner = {
    "0001101": 0, "0011001": 1, "0010011": 2,
    "0111101": 3, "0100011": 4, "0110001": 5,
    "0101111": 6, "0111011": 7, "0110111": 8,
    "0001011": 9
}

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    
    maze = []
    for _ in range(N):
        row = input().strip()
        if "1" in row:  # '1'이 포함된 행만 저장
            maze.append(row)
    
    if not maze:
        print(f"#{tc} 0")
        continue
    
    # 마지막 행을 사용하여 오른쪽 끝에서 첫 '1'의 위치를 찾음
    code_line = maze[-1]
    end = code_line.rfind("1")
    code_line = code_line[end - 55:end + 1]  # 56비트(7비트 * 8개)를 가져옴

    ans = []
    for i in range(0, 56, 7):
        segment = code_line[i:i + 7]
        if segment in scanner:
            ans.append(scanner[segment])
        else:
            ans = []
            break
    
    if len(ans) == 8:
        odd_sum = sum(ans[0::2])
        even_sum = sum(ans[1::2])
        result = odd_sum * 3 + even_sum

        if result % 10 == 0:
            print(f"#{tc} {sum(ans)}")
        else:
            print(f"#{tc} 0")
    else:
        print(f"#{tc} 0")
