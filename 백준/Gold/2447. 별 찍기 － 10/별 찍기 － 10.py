N = int(input())
arr = [['*']*N for _ in range(N)]
x = 0
y = 0

def star(N,x,y):
    a = x + (N//3)
    b = y + (N//3)

    for i in range(N//3):
        for j in range(N//3):
            arr[b+i][a+j] = " "
    
    if N > 3:
        for i in range(3):
            for j in range(3):
                star(N//3, x+(N//3)*j, y+(N//3)*i)
    else:
        return
    

star(N,x,y)

for i in range(N):
    ans = "".join(arr[i])
    print(ans)
