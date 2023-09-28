T = int(input())

for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    B = []
    now = 1
    
    for i in range(n):
        if A[i] == now:
            now += 1
        B.append(now)
        now += 1
    print(B[-1])