N = int(input())
A = list(map(int, input().split()))

cnt = 0

while True:
    A.sort(reverse=True)
    if len(A) >= 2 and A[0] > 0 and A[1] > 0:
        A[0] -= 1; A[1] -= 1
        cnt += 1
    elif A[0] > 0:
        A[0] -= 1
        cnt += 1
    else:
        break
if cnt > 1440:
    print(-1)
else:
    print(cnt)