A, B, C = map(int, input().split())

def DAC(A, B, C) :

    if B == 1 : return A % C
    else :
        if B % 2 == 0 : return (DAC(A, B//2, C)**2) % C
        else : return ((DAC(A, B//2, C)**2)*A) % C
        
print(DAC(A, B, C))