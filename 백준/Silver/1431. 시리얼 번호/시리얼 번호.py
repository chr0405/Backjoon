import sys
N = int(sys.stdin.readline().strip())
serialNumbers = [sys.stdin.readline().strip() for _ in range(N)]

# 숫자 합 계산 함수
def sum_of_digits(serial): 
    return sum(int(char) for char in serial if char.isdigit())

    # sum = 0
    # for char in sirial :
    #     if char.isdigit() :
    #         int(char)
    #         sum += char
    # return sum

def custom_sort_key(serial):
    return (len(serial), sum_of_digits(serial), serial) # 길이, 숫자 합, 사전 순 검색용 원본

serialNumbers.sort(key=custom_sort_key)

# 출력
for serial in serialNumbers:
    print(serial)