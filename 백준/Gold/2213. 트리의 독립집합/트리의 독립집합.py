import sys
sys.setrecursionlimit(10**6)
V = int(input())
w = list(map(int, input().split()))

tree = [[] for _ in range(V+1)]
dp = [[0]*2 for _ in range(V+1)]
ans = []

for i in range(V):
    dp[i+1][1] = w[i]
def dfs(cur, par):
    for node in tree[cur]:
        if node != par:
            dfs(node, cur)
            dp[cur][0] += max(dp[node])
            dp[cur][1] += dp[node][0]
for i in range(V-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
    
def path(cur, par, checker):
    if dp[cur][1] > dp[cur][0] and checker == True:
        ans.append(cur)
        checker = False
    else:
        checker = True
    
    for node in tree[cur]:
        if node != par:
            path(node, cur, checker)
            
dfs(1, 0)
path(1, 0, True)
ans.sort()    
print(max(dp[1]))
for i in ans:
    print(i, end = " ")
