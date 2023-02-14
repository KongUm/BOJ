N = int(input())

isPrime = [False, False] + [True]*(N-1)

for i in range(2, N+1):
    if isPrime[i]:
        for j in range(2*i, N+1, i):
            isPrime[j] = False
prime = []
for i in range(2,N+1):
    if isPrime[i]:
        prime.append(i)
    
dp = [0]*(N+1)
dp[0] = 1
for i in range(len(prime)):
    for j in range(1, N+1):
        if j-prime[i] >= 0:
            dp[j] += dp[j - prime[i]]
            dp[j] = dp[j]%123456789

print(dp[N])


 
