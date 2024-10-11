def isPalindrome(word):
    return word == word[::-1]

for testCase in range(1, 10 + 1):
    length = int(input().strip())  
    matrix = [list(input().strip()) for _ in range(8)] 
    answer = 0

    for row in range(8):
        for col in range(8 - length + 1):
            word = matrix[row][col:col + length]
            if isPalindrome(word):
                answer += 1

    for col in range(8):
        for row in range(8 - length + 1): 
            word = [matrix[row + i][col] for i in range(length)]  
            if isPalindrome(word):
                answer += 1

    print(f'#{testCase} {answer}')