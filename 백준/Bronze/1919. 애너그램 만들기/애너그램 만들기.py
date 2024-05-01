testCase1 = input()
testCase2 = input()

alphabetArray = [0]*26
count = 0

for alphabet in testCase1:
    alphabetArray[ord(alphabet)-97] += 1

for alphabet in testCase2:
    alphabetArray[ord(alphabet)-97] -= 1

for alphabet in alphabetArray:
    count += abs(alphabet)
print(count)