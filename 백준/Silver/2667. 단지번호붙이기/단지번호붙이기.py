N = int(input())
arr = []
V = []

S = [[0]*(N+2)]
for i in range(1,N+1):
    S.append([0])
    a = input()
    for j in range(len(a)):
        S[i].append(int(a[j]))
    S[i].append(0)
S.append([0]*(N+2))

b = [[0,1],[1,0],[0,-1],[-1,0]]
count = 1
for y in range(1,N+1):
    for x in range(1,N+1):
        if S[y][x] == 1:
            V.append(count)
            S[y][x] = count
            count += 1
            
E = [[] for _ in range(count)]
            
for y in range(1,N+1):
    for x in range(1,N+1):
        if S[y][x] != 0:
            for i in b:
                if S[y+i[0]][x+i[1]] != 0:
                    E[S[y][x]].append(S[y+i[0]][x+i[1]])
                    
visited = [False]*count

def dfs(R): # R = 시작노드
    global cnt
    visited[R] = True
    V.remove(R)
    cnt += 1
    for v in E[R]:
        if visited[v] == False:
            dfs(v)
ans = []
while len(V) != 0:
    cnt = 0
    dfs(V[0])
    ans.append(cnt)
print(len(ans))
ans.sort()
for i in ans:
    print(i)