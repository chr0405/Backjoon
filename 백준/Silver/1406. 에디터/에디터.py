import sys

settingString = list(sys.stdin.readline().rstrip())
temp = []

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if settingString:
            temp.append(settingString.pop())
    elif command[0] == 'D':
        if temp:
            settingString.append(temp.pop())
    elif command[0] == 'B':
        if settingString:
            settingString.pop()
    else:
        settingString.append(command[1])

settingString.extend(reversed(temp))
print(''.join(settingString))