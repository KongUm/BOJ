N = int(input())//2
arr = [list(map(int, input().replace("", " ").split())) for _ in range(N*2)]
global ans
ans = ""
a = 0
x = 0
y = 0

for i in range(N*2):
    a = a + sum(arr[i][0:N*2])

def qt(N, x, y):
    global ans

    ans = ans + "("

    for i in range(2):
        for j in range(2):
            S = 0
            if N == 1:
                S = arr[y+i][x+j]
            else:
                for p in range(N):
                    S = S + sum(arr[y + N * i + p][x + N * j : x + N * (j+1)])
                   
            if S == N**2:
                ans = ans + "1"
    
            elif S == 0:
                ans = ans + "0"

            else :
                qt(N//2, x+ N*j, y + N*i)

    ans = ans + ")"

qt(N, x, y)

if a == (N*2)**2:
    print("1")
elif a == 0:
    print("0")
else:
    print(ans)