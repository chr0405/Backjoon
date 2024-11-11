def backTracking(eggList, idx, count):
    global brokenCounter

    # 모든 계란을 부딪혔다면 현재까지 깨진 계란 수를 갱신
    if idx == len(eggList):
        brokenCounter = max(brokenCounter, count)
        return

    # 내구도가 0 이하라면 다음 계란으로 넘어감
    if eggList[idx][0] <= 0:
        backTracking(eggList, idx + 1, count)
        return

    # 다른 계란을 칠 수 있는지 확인
    any_broken = False
    for i in range(len(eggList)):
        # 현재 계란이 아니며 깨지지 않은 계란일 경우
        if i != idx and eggList[i][0] > 0:
            any_broken = True
            # 현재 계란과 i번째 계란을 부딪혀 봅니다.
            new_eggs = eggList[:]  # 원본 eggList 복사
            # 현재 계란의 내구도 갱신
            new_eggs[idx] = (new_eggs[idx][0] - new_eggs[i][1], new_eggs[idx][1])
            # 선택한 계란의 내구도 갱신
            new_eggs[i] = (new_eggs[i][0] - new_eggs[idx][1], new_eggs[i][1])

            # 깨진 계란 수를 갱신
            new_count = count
            if new_eggs[idx][0] <= 0:
                new_count += 1
            if new_eggs[i][0] <= 0:
                new_count += 1

            # 현재 계란을 그대로 두고, 다른 계란을 칠 수 있으면 재귀 호출
            backTracking(new_eggs, idx + 1, new_count)

    # 만약 아무 계란도 칠 수 없다면, 그 상태에서 결과를 갱신
    if not any_broken:
        brokenCounter = max(brokenCounter, count)

# 계란의 개수 입력
N = int(input())
eggList = []

# 계란의 내구도와 무게를 입력받습니다.
for _ in range(N):
    durability, weight = map(int, input().split())
    eggList.append((durability, weight))

# 깨진 계란 수를 기록할 변수
brokenCounter = 0

# eggList, 현재 계란 A의 index, 깨진 계란 수를 넘기며 백트래킹 시작
backTracking(eggList, 0, 0)

# 결과 출력
print(brokenCounter)
