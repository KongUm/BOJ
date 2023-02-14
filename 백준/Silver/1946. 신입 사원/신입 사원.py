import sys
T = int(input())

for _ in range(T):
    N = int(input())
    score = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
    score.sort()
    min_rank = N+1
    count = 0
    for i in range(N):
        if score[i][1] < min_rank:
            count += 1
            min_rank = score[i][1]
    print(count)