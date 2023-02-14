import sys
N = int(input())
S = list(map(int, input().split()))
S.insert(0,0)

dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    dp[i][i] = 1
for i in range(1,N):
    if S[i] == S[i+1]:
        dp[i][i+1] = 1

for c in range(1,N+1): # 개수
    for i in range(1,N-c+2): # 시작지점 // dp[i][i+c-1]
        if dp[i][i+c-1] == 0:
          
            continue
        if i-1 > 0 and i+c <= N:
            if S[i-1] == S[i+c]:   
                dp[i-1][i+c] = 1
M = int(input())
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[a][b])