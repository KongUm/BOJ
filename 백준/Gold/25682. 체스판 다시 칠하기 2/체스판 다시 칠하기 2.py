N, M, K = map(int, input().split())
# N = 세로, M = 가로
arr = [input() for _ in range(N)]

w_cnt = [[0]*M for _ in range(N)]
b_cnt = [[0]*M for _ in range(N)]

for y in range(N):
    for x in range(M):
        if (x+y) % 2 == 0: # 흰색
            if arr[y][x] == "B":
                w_cnt[y][x] = 1
        else:
            if arr[y][x] == "W":
                w_cnt[y][x] = 1
        if x != 0:
            w_cnt[y][x] = w_cnt[y][x] + w_cnt[y][x-1]
                
for y in range(N):
    for x in range(M):
        if (x+y) % 2 != 0: # 검은색
            if arr[y][x] == "B":
                b_cnt[y][x] = 1
        else:
            if arr[y][x] == "W":
                b_cnt[y][x] = 1
        if x != 0:
            b_cnt[y][x] = b_cnt[y][x] + b_cnt[y][x-1]
W = [[0]*M for _ in range(N)]
B = [[0]*M for _ in range(N)]
    
for y in range(N):
    for x in range(M):
        W[y][x] = w_cnt[y][x]
        B[y][x] = b_cnt[y][x]
        if y != 0:
            W[y][x] += W[y-1][x]
            B[y][x] += B[y-1][x]

            
mini = 99999999999999999
for i in range(N-K+1):
    for j in range(M-K+1):
        ws = W[i+K-1][j+K-1]
        bs = B[i+K-1][j+K-1]
        if i > 0:       
            ws -= W[i-1][j+K-1]
            bs -= B[i-1][j+K-1]
         
        if j > 0:
            ws -= W[i+K-1][j-1]
            bs -= B[i+K-1][j-1]
        if i > 0 and j > 0:
            ws += W[i-1][j-1]
            bs += B[i-1][j-1]
     
        mini = min(mini, ws, bs)
print(mini)