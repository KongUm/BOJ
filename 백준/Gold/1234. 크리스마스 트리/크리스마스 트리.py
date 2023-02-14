from math import factorial
N, R, G, B = map(int, input().split())
color = [R, G, B]

dp = [[[[0]*(B + 1) for _ in range(G + 1)] for _ in range(R + 1)] for _ in range(N + 1)]
# dp[r][g][b][i] = 레벨 i까지 꾸몄고, 각각 rgb개의 장식을 사용했을 때

two = [0]
three = [0]

for i in range(1, 10):
    p = factorial(2*i)//(factorial(i)*factorial(i))    
    q = factorial(3*i)//(factorial(i)*factorial(i)*factorial(i))
    two.append(p); three.append(q)

dp[0][0][0][0] = 1

for n in range(1, N + 1):
    for r in range(R + 1):
        for g in range(G + 1):
            for b in range(B + 1):
                #print(n, r, g, b)
                
                if n % 2 == 0:
                    a = n // 2
                    if r + a <= R and g + a <= G:
                        dp[n][r + a][g + a][b] += dp[n - 1][r][g][b]*two[a]
                    if g + a <= G and b + a <= B:
                        dp[n][r][g + a][b + a] += dp[n - 1][r][g][b]*two[a]        
                    if r + a <= R and b + a <= B:
                        dp[n][r + a][g][b + a] += dp[n - 1][r][g][b]*two[a]
                        
                if n % 3 == 0 and r + n//3 <= R and g + n//3 <= G and b + n//3 <= B:
                    a = n // 3             
                    dp[n][r+a][g+a][b+a] += dp[n - 1][r][g][b]*three[n//3]
                    
                if r + n <= R:
                    dp[n][r + n][g][b] += dp[n - 1][r][g][b]               
                if g + n <= G:
                    dp[n][r][g + n][b] += dp[n - 1][r][g][b]
                if b + n <= B:
                    dp[n][r][g][b + n] += dp[n - 1][r][g][b]

#print(dp[2][1][15][17])
cnt = 0
for i in range(R + 1):
    for j in range(G + 1):
        for u in range(B + 1):
            cnt += dp[N][i][j][u]
print(cnt)
                    
