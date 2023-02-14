arr = [[0] * 7 for _ in range(8)]
ty = [[[] for _ in range(7)] for _ in range(7)]
visited = [[False] * 7 for _ in range(8)]
res = 0
dy, dx = [0, -1], [-1, 0]

for y in range(8):
    s = input()
    for x in range(7):
        arr[y][x] = int(s[x])
        for i in range(2):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 8 and 0 <= nx < 7:
                t = [arr[y][x], arr[ny][nx]]; t.sort()
                ty[t[0]][t[1]].append((y, x, ny, nx))
                
def bt(a, b):
    global res, cnt
    if a == 6 and b == 6:
        res += 1
        return
    b += 1
    if b == 7:
        a += 1; b = a
        
    for y, x, ny, nx in ty[a][b]:
        if visited[y][x] == False and visited[ny][nx] == False:
            visited[y][x] = True; visited[ny][nx] = True
            bt(a, b)
            visited[y][x] = False; visited[ny][nx] = False
            
bt(0, -1)
print(res)