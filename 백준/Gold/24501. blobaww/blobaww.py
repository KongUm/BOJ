H, W = map(int, input().split())
arr = [input() for _ in range(H)]
dp = [[[0] * (W + 1) for _ in range(H + 1)] for _ in range(3)]

div = 1000000007
A = ['E', 'S', 'M']

for y in range(1, H + 1):
    for x in range(1, W + 1):
        if arr[y - 1][x - 1] == 'E':
            dp[0][y][x] = 1

def makePrefix(n):
    for y in range(1, H + 1):
        for x in range(1, W + 1):
            dp[n][y][x] = dp[n][y - 1][x] + dp[n][y][x - 1] - dp[n][y - 1][x - 1] + dp[n][y][x]
  
for n in range(1, 3):
    makePrefix(n - 1)
    for y in range(1, H + 1):
        for x in range(1, W + 1):
            if arr[y - 1][x - 1] == A[n]:
                dp[n][y][x] = dp[n - 1][y][x]

ans = 0
for y in range(1, H + 1):
    ans += sum(dp[2][y])
print(ans % div)