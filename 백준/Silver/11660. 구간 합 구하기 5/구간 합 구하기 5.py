import sys
N, M = map(int, input().split())
# 표의 크기 N*N

arr = [list(map(int, input().split())) for _ in range(N)]
sum_x = []
sum_arr = []
for y in range(N):
    A = []
    for x in range(N):
        if x == 0:
            A.append(arr[y][0])
        else:
            A.append(A[x-1] + arr[y][x])
    sum_x.append(A)
    
for x in range(N):
    B = []
    for y in range(N):
        if y == 0:
            B.append(sum_x[0][x])
        else:
            B.append(B[y-1] + sum_x[y][x])    
    sum_arr.append(B)

for i in range(M):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    
    ans = sum_arr[y2][x2]
    if x1 == 0 and y1 == 0:
        print(ans)
        continue
    elif x1 == 0:
        ans = ans - sum_arr[y1-1][x2]
    elif y1 == 0:
        ans = ans - sum_arr[y2][x1-1]
    else:
        ans = ans - sum_arr[y1-1][x2] - sum_arr[y2][x1-1] + sum_arr[y1-1][x1-1]
    print(ans)
