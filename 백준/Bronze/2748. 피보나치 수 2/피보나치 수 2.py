n = int(input())
dp = [0,1]
if n == 0:
    print(0)
else:
    for i in range(n-1):
        temp = dp[0] + dp[1]
        dp[0] = dp[1]
        dp[1]  = temp
    print(dp[1])