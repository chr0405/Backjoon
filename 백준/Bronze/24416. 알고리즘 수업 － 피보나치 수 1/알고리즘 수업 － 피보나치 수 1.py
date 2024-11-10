n = int(input())

def iterative_fib(x):
    first, second = 1, 1
    for _ in range(3, x + 1):
        first, second = second, first + second
    return second

def dp_count(x):
    return x - 2

print(iterative_fib(n), dp_count(n))
