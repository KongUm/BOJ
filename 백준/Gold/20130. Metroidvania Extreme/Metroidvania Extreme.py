from collections import deque
N, M = map(int, input().split())
# N = 세로 / M = 가로
arr = []
st = [0,0]
for y in range(N):
    S = input()
    temp = []
    for x in range(M):
        temp.append(S[x])
        if S[x] == "@":
            st = [y,x]
    arr.append(temp)

Q = deque()
key = set()
count = 1
ans = [[st[0],st[1]]]
wait = [[] for _ in range(26)]
dy = [1,-1,0,0]
dx = [0,0,1,-1]
def bfs():
    global count
    arr[st[0]][st[1]] = "0"
    Q.append([st[0]+1,st[1]])
    Q.append([st[0]-1,st[1]])
    Q.append([st[0],st[1]+1])
    Q.append([st[0],st[1]-1])
  
    while len(Q) != 0:
        u = Q.popleft() 
        ny, nx = u[0], u[1]
        loc = arr[ny][nx]
     
        if ord(loc) == 35 or loc == "0":
            continue
        elif 64 < ord(loc) < 91:
            if loc not in key:
              
                wait[ord(loc)-65].append([ny,nx])
                continue
            
        elif 96 < ord(loc) < 123:
            key.add(loc.upper())
            if len(wait[ord(loc)-97]) != 0:
                for w in wait[ord(loc)-97]:
               
                    Q.append(w)
        elif loc == "!":
            ans.append([ny,nx])
            count += 1
            return
 
        arr[ny][nx] = "0"
        count+= 1
        ans.append([ny,nx])
        for i in range(4):
            Q.append([ny+dy[i],nx+dx[i]])
bfs()
print(count)
for i in ans:
    print(i[0]+1, i[1]+1)
        