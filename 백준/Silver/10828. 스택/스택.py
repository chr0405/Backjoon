import sys

stack = []
pos = 0

for _ in range(int(sys.stdin.readline())): # N
    command = list(sys.stdin.readline().split())
    
    if command[0] == 'push':
        stack.append(command[1])
        pos += 1
    elif command[0] == 'pop':
        # stack에 아무 것도 없으면 0을 가르키고 있음
        if pos == 0 : print(-1)
        else :
            pos -= 1
            print(stack[pos])
            stack.pop()
    elif command[0] == 'size':
        print(pos)
    elif command[0] == 'empty':
        if pos == 0 : print(1)
        else : print(0)
    else :
        if pos == 0 : print(-1)
        else : print(stack[pos-1])
    