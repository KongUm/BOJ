R, C = map(int, input().split())

arr = []
alpha = set()
for _ in range(R):
    S = input()
    for i in range(C):
        alpha.add(S[i])
    arr.append(S)

len = len(alpha)

maxi = 1
visited = [False]*26
visited[ord(arr[0][0])-65] = True
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def BT(x, y, cnt):
    global maxi
    maxi = max(maxi, cnt)
    if maxi == len:
        print(len)
        exit()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and visited[ord(arr[ny][nx])-65] == False:
            visited[ord(arr[ny][nx])-65] = True
            BT(nx, ny, cnt + 1)
            visited[ord(arr[ny][nx])-65] = False
    return
BT(0,0,1)
print(maxi)