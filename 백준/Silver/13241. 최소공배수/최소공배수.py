import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def GCD(A, B):
  while A * B != 0:
    if A > B:
      A = A % B
    else:
      B = B % A
  return A + B

G = GCD(A, B)
L = int((A * B) / G)

print(L)