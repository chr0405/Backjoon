import sys

def can_serve_snacks():
    N = int(sys.stdin.readline().strip())
    students = list(map(int, sys.stdin.readline().split()))

    stack = []
    current = 1

    for student in students:
        while stack and stack[-1] == current:
            stack.pop()
            current += 1

        if student == current:
            current += 1
        else:
            stack.append(student)

    while stack and stack[-1] == current:
        stack.pop()
        current += 1

    return "Nice" if not stack else "Sad"

result = can_serve_snacks()
print(result)