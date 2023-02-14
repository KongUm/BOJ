import math
N = int(input())
s = [int(input()) for _ in range(N)]
K = int(input())

dp = [[0]*K for _ in range(1 << N)]
leng = [0]*(1 << N)

mod = []
for i in range(1 << N):
    a = ""
    for j in range(N):
        if i & (1 << j) != 0:
            a += str(s[j])
    leng[i] += len(a)


for i in range(1000):
    mod.append(10**i % K)

for i in range(N):
    dp[1 << i][s[i] % K] += 1

for i in range(1, (1 << N)-1):
    for j in range(N):
        if i & (1 << j) == 0:
            for r in range(K):
                dp[i + (1 << j)][(r % K + (s[j] % K * mod[leng[i]]) % K) % K] += dp[i][r]


a = dp[(1 << N) - 1][0]
b = math.factorial(N)
c = math.gcd(a, b)

if a == b:
    print("1/1")
elif a == 0:
    print("0/1")
else:
    print(str(a//c) + "/" + str(b//c))
