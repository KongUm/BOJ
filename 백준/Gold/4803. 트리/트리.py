import sys
checker = True
count = 0
def dfs(R, before):
    global visited
    global checker 
    visited[R] = True
    
    for x in tree[R]:
        if visited[x] == True:
            if x != before:
                checker = False
        else:
            dfs(x, R)
    return
    
while True:
    V, E = map(int, sys.stdin.readline().split())
    if V == 0 and E == 0:
        exit()
    count += 1
    tree = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)
        
    cnt = 0
    visited = [False]*(V+1)
    
    for i in range(1, V+1):
        if visited[i] == False:
            checker = True
            dfs(i, i)
            
            if checker:
                cnt += 1
    
    if cnt == 0:
        print("Case " + str(count) + ": No trees.")
    elif cnt == 1:
        print("Case " + str(count) + ": There is one tree.")
    else:
        print("Case " + str(count) + ": A forest of " + str(cnt) + " trees.")
    
    
    