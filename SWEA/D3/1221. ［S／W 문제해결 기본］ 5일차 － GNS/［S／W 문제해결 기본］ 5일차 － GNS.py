T = int(input().strip())

dict = {
    'ZRO': 0, 'ONE': 1, 'TWO': 2,
    'THR': 3, 'FOR': 4, 'FIV': 5,
    'SIX': 6, 'SVN': 7, 'EGT': 8,
    'NIN': 9
}

for _ in range(T):
    tcNum, tcCount = map(str, input().split())
    tcList = list(map(str, input().split()))

    tcList.sort(key=lambda x: dict[x])

    answer = ' '.join(tcList)
    print(f'{tcNum} {answer}')
