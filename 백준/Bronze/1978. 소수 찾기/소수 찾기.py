N = int(input())
Numbers = map(int, input().split())
Answer = 0
for Num in Numbers:
    error = 0
    if Num > 1 :
        for i in range(2, Num):
            if Num % i == 0:
                error += 1 
        if error == 0:
            Answer += 1 
print(Answer)