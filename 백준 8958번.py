n = int(input())
import sys




for i in range(n):
    a = sys.stdin.readline().rstrip()
    b = list(a)
    score = 0
    stack = 1
    for j in b:
        if j == 'O':
            score += stack
            stack += 1

        else:
            stack = 1

    print(score)

