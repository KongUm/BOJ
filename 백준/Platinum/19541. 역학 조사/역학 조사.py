import sys
N, M = map(int, input().split())

progress = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
info = [0] + list(map(int, sys.stdin.readline().split()))
table = info[:]

for i in range(M-1, -1, -1):
    k = progress[i][0]
    type = 1
    for j in range(1,k+1):
        if table[progress[i][j]] == 0:
            type = 0
            break
    if type == 0:
        for j in range(1,k+1):
            table[progress[i][j]] = type

infect = table[:]
      
for i in range(M):
    k = progress[i][0]
    type = 0
    for j in range(1, k+1):
        if infect[progress[i][j]] == 1:
            type = 1
            break
    if type == 1:
        for j in range(1, k+1):
            infect[progress[i][j]] = type

checker = True
isone = [False, False]
iszero = [False, False]
for i in range(1,N+1):
    if info[i] != infect[i] or (info[i] == 0 and table[i] == 1):
        checker = False
        break
    if info[i] == 0:
        iszero[0] = True
    if info[i] == 1:
        isone[0] = True
    if table[i] == 0:
        iszero[1] = True
    if table[i] == 1:
        isone[1] = True
if checker == False or iszero[0] != iszero[1] or isone[0] != isone[1]:
    print("NO")
else:
    print("YES")
    for i in range(1,N+1):
        print(table[i], end = " ")
    
    