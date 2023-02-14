N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
x = 0
y = 0
global minus, zero, one
minus = 0
zero = 0
one = 0
pa = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

def paper(N, x, y):
    global minus, zero, one
    std = arr[y][x] 
    checker = True

    for y2 in range(N):
        for x2 in range(N):
            if std != arr[y+y2][x+x2]:
                checker = False
                break
        if checker == False:
            break                  
                            
    if checker == True:
        if std == -1:
            minus = minus + 1
        elif std == 0:
            zero = zero + 1
        else:
            one = one + 1
        if N == 1:
            return
    else:
        for i in range(9):   
            paper(N//3, x+(N//3)*pa[i][0], y+(N//3)*pa[i][1])
            
paper(N,x,y)

print(minus)
print(zero)
print(one)