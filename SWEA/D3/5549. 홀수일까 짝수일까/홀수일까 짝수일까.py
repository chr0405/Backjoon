T = int(input())

for t in range(1, T + 1):
    number = input().strip()
    
    if int(number[-1]) % 2 == 0:
        print(f"#{t} Even")
    else:
        print(f"#{t} Odd")
