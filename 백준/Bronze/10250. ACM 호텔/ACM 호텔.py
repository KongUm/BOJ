T = int(input())
A = list(list(map(int, input().split())) for _ in range(T))

for i in range(T):
    H = A[i][0]
    N = A[i][2]
    q = N // H
    r = N % H
    if r == 0:
        ans = str(H)
        if q < 10:
            ans = ans + "0" + str(q)
        else:
            ans = ans + str(q)
        print(ans)
    else:
        ans = str(r)
        if q+1 < 10:
            ans = ans + "0" + str(q+1)
        else:
            ans = ans + str(q+1)
        print(ans)
