N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
x = 0
y = 0
global t
t = 1

def div(N, x, y):

    global t

    if N < 1:
        return

    S = 0
    for i in range(N):
        S = S + sum(arr[x+i][y:y+N])

    if S == N**2:
        return 1

    elif S == 0:
        return 0 

    elif N >= 2 and S != N**2:
        t = t+3
        return div(N//2, x, y) + div(N//2, x+(N//2), y) + div(N//2, x, y+(N//2)) + div(N//2, x+(N//2), y+(N//2))
    else:
        return 0



blue = div(N, x, y)

print(t-blue)
print(blue)