T = int(input().strip())

numberDict = {
    '0001101': 0, '0011001': 1, '0010011': 2,
    '0111101': 3, '0100011': 4, '0110001': 5,
    '0101111': 6, '0111011': 7, '0110111': 8,
    '0001011': 9
}

for i in range(1, T + 1):
    N, M = map(int, input().split())
    
    totalArray = [input().strip() for _ in range(N)]
    codeArray = None
    for row in totalArray:
        if '1' in row:  # 암호 코드가 있는 줄 찾기
            last_one_index = row.rfind('1')
            codeArray = row[last_one_index - 55:last_one_index + 1]
            break
    
    # 암호를 7자리씩 분리하여 숫자로 변환
    decoded_digits = []
    for j in range(0, 56, 7):
        segment = codeArray[j:j+7]
        if segment in numberDict:
            decoded_digits.append(numberDict[segment])
    
    # 홀수 자리와 짝수 자리 합산
    oddCount = sum(decoded_digits[k] for k in range(0, len(decoded_digits), 2))
    evenCount = sum(decoded_digits[k] for k in range(1, len(decoded_digits), 2))

    # 검증 코드
    if (oddCount * 3 + evenCount) % 10 == 0:
        answer = sum(decoded_digits)
    else:
        answer = 0
    
    print(f'#{i} {answer}')
