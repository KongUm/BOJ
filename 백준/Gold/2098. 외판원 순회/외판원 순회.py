N = int(input())
w = [list(map(int, input().split())) for _ in range(N)]

memo = [[0] * (1 << N) for _ in range(N)]
INF, end = int(1e9), (1 << N) - 1


def travel(now, visited):
    if visited == end:
        if w[now][0] > 0:
            return w[now][0]
        else:
            return INF

    if memo[now][visited] != 0:
        return memo[now][visited]

    memo[now][visited] = INF

    for i in range(N):
        if w[now][i] == 0 or visited & (1 << i) != 0:
            continue
        temp = travel(i, visited | 1 << i)
        memo[now][visited] = min(memo[now][visited], w[now][i] + temp)

    return memo[now][visited]

print(travel(0, 1))