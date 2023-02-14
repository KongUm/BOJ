import sys
N, K = map(int, input().split())

coin = []
for _ in range(N):
    c = int(sys.stdin.readline())
    if c <= K:
        coin.append(c)
coin.sort()

dp = [10**6]*(K+1) # dp[i] = 동전 가치의 합이 i가 되도록 하는 동전의 최소 갯수
dp[0] = 0
for i in range(len(coin)):
    for j in range(1,K+1):
        if j-coin[i] >= 0:
            dp[j] = min(dp[j-coin[i]] + 1, dp[j])

if dp[K] > 10**5:
    print(-1)
else:
    print(dp[K])
    
