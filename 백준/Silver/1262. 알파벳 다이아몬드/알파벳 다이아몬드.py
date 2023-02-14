N, y1, x1, y2, x2 = map(int, input().split())
dx, dy = x2-x1+1, y2-y1+1

arr = [['.']*dx for _ in range(dy)]

for y in range(y1,y2+1):
    for x in range(x1,x2+1):
        if x % (N*2-1) < N:
            ax = (N-1) - (x%(N*2-1))
        else:
            ax = (x%(N*2-1)) - (N-1)
            
        if y % (N*2-1) < N:
            ay = (N-1) - (y%(N*2-1))
        else:
            ay = (y%(N*2-1)) - (N-1)
        ascii = (ax+ay)%26
        if ax+ay < N:
            arr[y-y1][x-x1] = chr(ascii+97)
        else:
            arr[y-y1][x-x1] = '.'
for i in range(dy):
    print("".join(arr[i]))