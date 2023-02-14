from collections import deque

S = int(input())

visited = [[False]*(S+1) for _ in range(S+1)]
Q = deque()

visited[0][0] = True
Q.append([1, 0, 0])

while len(Q) > 0:
    now, clip, cnt = Q.popleft()
    if now == S:
        print(cnt)
        exit()   
        
    if clip > 0 and now + clip <= S and visited[now+clip][clip] == False:
        Q.append([now + clip, clip, cnt+1])
        visited[now+clip][clip] = True
        
    if now > 1 and visited[now-1][clip] == False:
        Q.append([now-1, clip, cnt+1])
        visited[now-1][clip] = True
        
    if visited[now][now] == False:
        Q.append([now, now, cnt+1])
        visited[now][now] = True
