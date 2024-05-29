import sys

while 1:

  testCase = sys.stdin.readline().rstrip()

  result = ''

  if testCase == '.':
    break

  for char in testCase:
    if char not in '()[]':
      continue
    else:
      result += char

  for _ in range(len(result) // 2 + 1):
    result = result.replace('()', '')
    result = result.replace('[]', '')

  if len(result):
    print('no')
  else:
    print('yes')