from itertools import permutations
n, k = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
idx = [i for i in range(n)]
now = 500
cnt = 0

for p in permutations(idx): 
    now = 500
    for i in range(n):
        now += A[idx[p[i]]] - k     
        if now < 500:
            break

    if now >= 500:
        cnt += 1
        
print(cnt)