from collections import deque
row = [set() for _ in range(9)] # 행 : 가로축
column = [set() for _ in range(9)] # 열 : 세로축
square = [set() for _ in range(9)]
A = [input() for _ in range(9)]
empty = deque() #empty는 왼쪽 위부터 오른쪽 아래순서로 들어있다

arr = [[0]*9 for _ in range(9)]
for y in range(9):
    for x in range(9):
        arr[y][x] = int(A[y][x])

for y in range(9):
    for x in range(9):
        if arr[y][x] != 0:
            row[y].add(arr[y][x])
            column[x].add(arr[y][x])
            a = (y//3)*3 + x//3 
            square[a].add(arr[y][x])
        else:
            empty.append([x,y])
            

def dfs():
    
    if len(empty) == 0:
        for i in range(9):
            for j in range(9):
                if j != 8:
                    print(arr[i][j], end = "")
                else:
                    print(arr[i][j])
        exit(0)
        return 
    else:
        u = empty.popleft()
        x, y = u[0], u[1]
        a = (y//3)*3 + x//3 
        for i in range(1,9+1):
            if i in row[y] or i in column[x] or i in square[a]:
                continue
            else:
                row[y].add(i)
                column[x].add(i)
                square[a].add(i)
            arr[y][x] = i
            dfs()
            
            row[y].remove(i)
            column[x].remove(i)
            square[a].remove(i)
            arr[y][x] = 0
        empty.appendleft([x,y])
    
            
dfs()
