import sys
sys.setrecursionlimit(10**7)
V = int(input())

tree = [[] for _ in range(V+1)]
dp = [[0]*2 for _ in range(V+1)]
# dp[i][j] = i번째 노드가 루트인 서브 트리에서
# j = 0: i번째 노드를 선택했을 때 최솟값 / j = 1: i번째 노드를 선택하지 않았을 때 최솟값

for _ in range(V-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
    
for i in range(1,V+1):
    dp[i][1] = 1

def dfs(cur, par):
    for node in tree[cur]:
        if node != par:
            dfs(node, cur)
            dp[cur][0] += dp[node][1]
            dp[cur][1] += min(dp[node][0], dp[node][1])
   
dfs(1, 0)
print(min(dp[1]))