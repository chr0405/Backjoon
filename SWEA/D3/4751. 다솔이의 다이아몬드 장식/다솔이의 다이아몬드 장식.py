t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    print('..#.' * n + '.')
    print('.#.#' * n + '.')
    print('#.' + '.#.'.join(s) + '.#')
    print('.#.#' * n + '.')
    print('..#.' * n + '.')
