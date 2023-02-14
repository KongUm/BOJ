N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
w = [[0] * N for _ in range(N)]
memo = [[0]*N for _ in range(1 << N)] # memo[visited][i]
INF, end = int(1e9), (1 << N) - 1

for i in range(N):  # 출발 도시 선택
    for j in range(N):  # 도착 도시 선택
        if i == j:
            w[i][j] = INF
            continue
        x, y = A[i][0] - A[j][0], A[i][1] - A[j][1]
        w[i][j] = ((x**2) + (y**2))**0.5


def travel(now, visited):
    if visited == end:
        return w[now][0]

    if memo[visited][now] != 0:
        return memo[visited][now]

    memo[visited][now] = INF

    for i in range(N):
        if w[now][i] == INF or visited & (1 << i) != 0:
            continue
        temp = travel(i, visited | (1 << i))
        memo[visited][now] = min(memo[visited][now], w[now][i] + temp)
    return memo[visited][now]

print(travel(0, 1))