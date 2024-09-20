import sys

N = int(sys.stdin.readline().strip())
meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 회의가 끝나는 시간이 짧은 순, 끝나는 시간이 같으면 일찍 시작하는 순
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
endTime = 0

for start, end in meetings:
    if start >= endTime:  # 회의가 끝난 이후에 시작할 수 있는지
        endTime = end
        count += 1

print(count)