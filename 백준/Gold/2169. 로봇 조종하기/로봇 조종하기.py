N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*M for _ in range(N)]
# dp[y][x] = (y, x) 의 좌표에 도달 했을 때 가치의 합의 최댓값

dp[0][0] = arr[0][0]
for i in range(1, M):
    dp[0][i] = dp[0][i - 1] + arr[0][i]

for y in range(1, N):
    left, right = [-int(1e9)]*M, [-int(1e9)]*M

    for x in range(M):
        left[x] = dp[y - 1][x] + arr[y][x]
        if x > 0:
            left[x] = max(left[x - 1] + arr[y][x], left[x])

    for x in range(M - 1, -1, -1):
        right[x] = dp[y - 1][x] + arr[y][x]
        if x < M - 1:
            right[x] = max(right[x + 1] + arr[y][x], right[x])

    for x in range(M):
        dp[y][x] = max(left[x], right[x])
print(dp[N - 1][M - 1])


