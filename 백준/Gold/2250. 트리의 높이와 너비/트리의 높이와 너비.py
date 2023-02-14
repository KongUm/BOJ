N = int(input()) # 노드의 수

graph = [[-1, -1] for _ in range(N + 1)]

for _ in range(N):
    n, l, r = map(int, input().split())
    graph[n] = [l, r]

level = 0
info = [[int(1e9), 0] for _ in range(N + 1)]
cnt = 1

def preorder(node, l):
    global cnt
    if graph[node][0] != -1:
        preorder(graph[node][0], l + 1)
        
    info[l][0] = min(info[l][0], cnt)
    info[l][1] = max(info[l][1], cnt)
    cnt += 1

    if graph[node][1] != -1:
        preorder(graph[node][1], l + 1)

checker = [True]*(N + 1)
for i in range(1, N + 1):
    for j in graph[i]:
        if j > 0:
            checker[j] = False

for i in range(1, N + 1):
    if checker[i]:
        preorder(i, 0)
    
ans = [0, 0]

for i in range(N):
    if info[i][1] - info[i][0] > ans[1]:
        ans = [i, info[i][1] - info[i][0]]
print(ans[0] + 1, ans[1]+1)
