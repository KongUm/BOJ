import sys
sys.setrecursionlimit(10**6)
V = int(input())
w = list(map(int, input().split()))

tree = [[] for _ in range(V+1)]
dp = [[0]*2 for _ in range(V+1)]

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
dfs(1, 0)
print(max(dp[1]))