import sys

L, C = map(int, sys.stdin.readline().split())
array = sys.stdin.readline().split()
array.sort()
passwordArray = []
vowels = ['a', 'i', 'u', 'e', 'o']

def backTracking(start):

    if len(passwordArray) == L :
        vowelCount = 0

        for j in passwordArray:
            if j in vowels:
                vowelCount += 1
        
        consonantCount = L - vowelCount
        
        if vowelCount >= 1 and consonantCount >= 2:
            print("".join(passwordArray))
        return
    
    for i in range(start, C):
        passwordArray.append(array[i])
        backTracking(i + 1)
        passwordArray.pop()

backTracking(0)