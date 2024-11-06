def isPalindrome(word):
    return word == word[::-1]
 
for _ in range(1, 10 + 1):
    testCase = int(input().strip())  
    
    matrix = [list(input().strip()) for _ in range(100)]
    matrix_reverse = list(zip(*matrix))
    matrixMax = 0
    matrix_reverseMax = 0
    maxLen = 0
 
    for row in range(100):
        for col in range(100):
            for k in range(col+1, 101):
                if isPalindrome(matrix[row][col:k]):
                    matrixMax = len(matrix[row][col:k])
                if isPalindrome(matrix_reverse[row][col:k]):
                    matrix_reverseMax = len(matrix_reverse[row][col:k])
                maxLen = max(maxLen, matrixMax, matrix_reverseMax)
 
    print(f'#{testCase} {maxLen}')