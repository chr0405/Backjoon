n = int(input())
chat = [input().strip() for _ in range(n)]

greetings = 0
users = set()

for message in chat:
    if message == "ENTER":
        users = set()
    else:
        if message not in users:
            greetings += 1
            users.add(message)

print(greetings)
