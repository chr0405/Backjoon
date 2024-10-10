T = int(input().strip())
aeiou = ['a', 'e', 'i', 'o', 'u']

for i in range(1, T+1):
    word = input().strip()
    answer = []
    
    for j in word:
        if j not in aeiou:
            answer.append(j)
    
    answer = ''.join(answer)
	
    print(f'#{i} {answer}')