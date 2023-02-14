import sys
inp = []
t = 0
while True:
    p = list(map(int, sys.stdin.readline().split()))
    inp.append(p)
    t = t+1
    if p == [-1,-1,-1]:
        break

arr = [[[0 for k in range(21)] for j in range(21)]for i in range(21)]

def w(a,b,c):
    global arr
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    elif arr[a][b][c] != 0:
        return arr[a][b][c]
    elif a < b and b < c:
        arr[a][b][c] =  w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return arr[a][b][c]
    else:
        arr[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
        return arr[a][b][c]

for i in range(t-1):
    print(f"w({inp[i][0]}, {inp[i][1]}, {inp[i][2]}) = {w(inp[i][0],inp[i][1],inp[i][2])}")    