N,M = map(int,input().split())
arr = [input() for _ in range(N)]
c_list = []

for i in range(N-7):
    for j in range(M-7):
        change = 0
        for p in range(8): #i는 y축
            for q in range(8): #j는 X축
                x = q+j
                y = p+i
                if (x%2 + y%2)%2 == 0:
                    if arr[y][x] == "W":
                        change = change + 1
                else:
                    if arr[y][x] == "B":
                        change = change + 1
        if change < 64-change:
            c_list.append(change)
        else:
            c_list.append(64-change)

print(min(c_list))