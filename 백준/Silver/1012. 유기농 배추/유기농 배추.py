import sys
T = int(input())

xy = [[0,1],[1,0],[-1,0],[0,-1]]

def DFS(x,y):
    global K
    if graph[y][x] == 1:
        graph[y][x] = 0
        loca.remove([x,y])
        for i in xy:
            DFS(x+i[0], y+i[1])

for _ in range(T):
    M, N, K = map(int, input().split())
    # M = 가로, N = 세로, K = 배추가 심어져 있는 위치의 개수 (node)
    loca = []
    graph = [[0]*(M+2) for _ in range(N+2)]
    
    for i in range(K):
        loca.append(list(map(int, sys.stdin.readline().split())))
        loca[i][0] += 1
        loca[i][1] += 1
        graph[loca[i][1]][loca[i][0]] = 1
        
    count = 0    
    while len(loca) != 0:
        DFS(loca[0][0],loca[0][1])
        count += 1
    print(count)