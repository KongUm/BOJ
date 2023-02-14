R, C, N = map(int, input().split())
# R = 세로길이, C = 가로길이, N = N초가 지난 후

arr = [[] for _ in range(R)]

cnt = 1
for i in range(R):
    s = input()
    for j in range(C):
        if s[j] == 'O':
            arr[i].append(2)
        else:
            arr[i].append(-1)
            
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for t in range(2,N+1):
    if t % 2 == 0: # 짝수 초 일때는 폭탄 설치
        for y in range(R):
            for x in range(C):
                if arr[y][x] == -1:
                    arr[y][x] = 0
    else: # 홀수 초 일때는 폭발
        for y in range(R):
            for x in range(C):
                if arr[y][x] == 3: # 3초 짜리 폭탄 폭발
                    arr[y][x] = -1
                    for i in range(4):
                        if x+dx[i] < 0 or x+dx[i] >= C or y+dy[i] < 0 or y+dy[i] >= R:
                            continue
                        if arr[y+dy[i]][x+dx[i]] != 3:
        
                            arr[y+dy[i]][x+dx[i]] = -1
    for y in range(R):
        for x in range(C):
            if arr[y][x] >= 0:
                arr[y][x] += 1

for y in range(R):
    for x in range(C):
        if arr[y][x] == -1:
            print('.', end = "")
        else:
            print('O', end = "")
    print()    