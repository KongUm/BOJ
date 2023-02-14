import sys

T = int(input())

for _ in range(T):
    sx1, sy1, sx2, sy2 = map(int, input().split())
    cnt = 0
    N = int(input())
    for i in range(N):
        x, y, r = map(int, sys.stdin.readline().split())
        d1 = (sx1 - x) ** 2 + (sy1 - y) ** 2
        d2 = (sx2 - x) ** 2 + (sy2 - y) ** 2
        if (d1 < r ** 2 and d2 > r ** 2) or (d1 > r ** 2 and d2 < r ** 2):
            cnt += 1
    print(cnt)