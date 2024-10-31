import sys
input = sys.stdin.read

data = input().strip().splitlines()
n = int(data[0]) 

dancers = set()
dancers.add("ChongChong") 

for line in data[1:]:
    person1, person2 = line.split()
    
    if person1 in dancers or person2 in dancers:
        dancers.add(person1)
        dancers.add(person2)

print(len(dancers))