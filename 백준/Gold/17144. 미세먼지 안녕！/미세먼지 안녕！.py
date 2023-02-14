import sys
R, C, T = map(int, input().split())
# R = 세로, C = 가로

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
cx = []
cy = []
for y in range(R):
    for x in range(C):
        if arr[y][x] == -1:
            cx.append(x) # index 0번이 더 위쪽에 있음
            cy.append(y)
            
temp = [[0]*C for _ in range(R)]
for time in range(T):
    temp = [[0]*C for _ in range(R)]
 
    for y in range(R):
        for x in range(C):
            if arr[y][x] > 0:
                target = arr[y][x]
                diff = target//5
                             
                if x != 0 and (x-1 not in cx or y not in cy):
                    temp[y][x-1] += diff
                    target -= diff
                if x != C-1 and (x+1 not in cx or y not in cy):
                    temp[y][x+1] += diff
                    target -= diff
                if y != 0 and (x not in cx or y-1 not in cy):
                    temp[y-1][x] += diff
                    target -= diff
                if y != R-1 and (x not in cx or y+1 not in cy):
                    temp[y+1][x] += diff
                    target -= diff
                temp[y][x] += target
            #print(temp)
    for i in range(cy[0]-1,-1,-1): 
        temp[i+1][0] = temp[i][0]
    for i in range(cy[1]+1,R):
        temp[i-1][0] = temp[i][0]
    for i in range(1,C):
        temp[0][i-1] = temp[0][i]
        temp[R-1][i-1] = temp[R-1][i]
    for i in range(1,cy[0]+1):
        temp[i-1][C-1] = temp[i][C-1]
    for i in range(R-2,cy[1]-1,-1):
        temp[i+1][C-1] = temp[i][C-1]
    for i in range(C-2,0,-1):
        temp[cy[0]][i+1] = temp[cy[0]][i]
        temp[cy[1]][i+1] = temp[cy[1]][i]
    temp[cy[0]][0] = -1
    temp[cy[1]][0] = -1
    temp[cy[0]][1] = 0
    temp[cy[1]][1] = 0
                
    arr = [copy[:] for copy in temp]
ans = 0
for i in range(R):
    ans += sum(arr[i])
print(ans+2)

                    
                    
                           
