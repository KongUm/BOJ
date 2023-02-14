N = int(input())
W = int(input())
inc = [[1,1]] + [list(map(int, input().split())) for _ in range(W)]
inc2 = inc[:]
inc2[0] = [N, N]

dp = [[int(1e9)]*(W+1) for _ in range(W+1)]
path = [[[0]*2 for _ in range(W+1)] for _ in range(W+1)]
# dp[i][j] = 경찰차 1의 위치가 i번째 사건, 경찰차 2의 위치가 j번째 사건일 때

dp[1][0] = abs(sum(inc[1]) - sum(inc[0]))
dp[0][1] = abs(sum(inc2[1]) - sum(inc2[0]))

for p in range(1, W + 1): # 현재 사건
    # 경찰차 1을 움직일때
    for i in range(p - 1):

        if dp[p - 1][i] + abs(inc[p-1][0] - inc[p][0]) + abs(inc[p-1][1] - inc[p][1]) < dp[p][i]:
            dp[p][i] = dp[p - 1][i] + abs(inc[p-1][0] - inc[p][0]) + abs(inc[p-1][1] - inc[p][1])
            path[p][i] = [p - 1, i]

        if dp[i][p - 1] + abs(inc[p][0] - inc[i][0]) + abs(inc[p][1] - inc[i][1]) < dp[p][p - 1]:
            dp[p][p - 1] = dp[i][p - 1] + abs(inc[p][0] - inc[i][0]) + abs(inc[p][1] - inc[i][1])
            path[p][p - 1] = [i, p - 1]

        if dp[i][p - 1] + abs(inc2[p][0] - inc2[p - 1][0]) + abs(inc2[p][1] - inc2[p - 1][1]) < dp[i][p]:
            dp[i][p] = dp[i][p - 1] + abs(inc2[p][0] - inc2[p - 1][0]) + abs(inc2[p][1] - inc2[p - 1][1])
            path[i][p] = [i, p - 1]

        if dp[p - 1][i] + abs(inc2[p][0] - inc2[i][0]) + abs(inc2[p][1] - inc2[i][1]) < dp[p - 1][p]:
            dp[p - 1][p] = dp[p - 1][i] + abs(inc2[p][0] - inc2[i][0]) + abs(inc2[p][1] - inc2[i][1])
            path[p - 1][p] = [p - 1, i]


a, b = 0, 0
ans = int(1e9)
for p in range(W):

    if dp[p][W] <= ans:
        a, b = p, W
        ans = dp[p][W]
    if dp[W][p] <= ans:
        a, b = W, p
        ans = dp[W][p]

trace = []

while a + b > 0:
    na, nb = path[a][b]
    if na < a:
        trace.append(1)
    else:
        trace.append(2)
    a, b = na, nb

print(ans)
for p in range(len(trace) - 1, -1, -1):
    print(trace[p])


