import sys
N, K = map(int, input().split())

coin = []
for _ in range(N):
    c = int(sys.stdin.readline())
    if c <= K:
        coin.append(c)
coin.sort()

dp = [0]*(K+1) # dp[i] = 동전 가치의 합이 i가 되도록 하는 경우의 수

dp[0] = 1 # 동전이 아무것도 없는 상태에서 가져올 수 있으므로 

for i in range(len(coin)):
    for j in range(1,K+1):
        if j-coin[i] >= 0:
            dp[j] += dp[j-coin[i]] 
print(dp[K])
    
