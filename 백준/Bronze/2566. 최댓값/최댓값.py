
A = [list(map(int, input().split())) for _ in range(9)]
maxi = -1
yx = [-1,-1]
for i in range(9):
    for j in range(9):
        if A[i][j] > maxi:
            maxi = A[i][j]
            yx = [j,i]
print(maxi)
print(yx[1]+1,yx[0]+1)
            