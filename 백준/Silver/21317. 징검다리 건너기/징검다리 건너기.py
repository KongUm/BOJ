import sys
N = int(input())
rock = [] # rock[0] = 작은 점프, rock[1] = 큰 점프
for i in range(N-1):
    rock.append(list(map(int, sys.stdin.readline().split())))
K = int(input())

dp = [[0,0]] # dp[i] = i번째 돌까지 올때 필요한 에너지 (0~N)

for i in range(1,N):
    dp.append([0,0])
    if i == 1:
        dp[i][0] = (dp[i-1][0] + rock[i-1][0]) # 작은점프
        dp[i][1] = 100000000000
    
    if i >= 2:
        a = dp[i-1][0] + rock[i-1][0]
        b = dp[i-2][0] + rock[i-2][1] # 큰 점프
        dp[i][0] = min(a,b)
        dp[i][1] = 100000000000
        
    if i >= 3:
        A = dp[i-1][1] + rock[i-1][0]
        B = dp[i-2][1] + rock[i-2][1]
        C = dp[i-3][0] + K
        dp[i][1] = min(A,B,C)
print(min(dp[N-1]))

