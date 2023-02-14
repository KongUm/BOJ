N = int(input())

dp = [1,3]
for i in range(N-2):
    if i % 2 == 0:
        ans = (dp[1]*2 -1)%10007
    else:
        ans = (dp[1]*2 +1)%10007
    dp[0] = dp[1]
    dp[1] = ans

if N == 1:
    print(1)
else:
    print(dp[1])

    