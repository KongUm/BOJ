n = int(input())
wine = [0]

for _ in range(n):
    wine.append(int(input()))

dp = [[0]*3 for _ in range(n+1)]
# dp[i][j] = i번째 포도주까지 마셨을때 + j+번 연속으로

dp[1][1] = wine[1]
if n>=2:
    dp[2][1] = wine[2]
if n>=3:
    dp[3][1] = wine[1] + wine[3]
    dp[3][2] = wine[2] + wine[3]
    
for i in range(2,n+1):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = wine[i] + max(dp[i-2])
    dp[i][2] = wine[i] + dp[i-1][1]
            
print(max(max(dp[n]),max(dp[n-1]),max(dp[n-2])))
