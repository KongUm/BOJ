A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for m in range(3): # 배율
    for i in range(3): # 0 = chiecken, 1 = pizza, 2 = ham
        if A[(i + m)%3] >= 0 and B[i]//(3**m) >= 0:
            if A[(i + m)%3] - B[i]//(3**m) < 0:
                cnt += A[(i + m)%3]
                B[i] -= A[(i + m)%3]*(3**m)
                A[(i + m) % 3] = 0
            else:
                A[(i + m)%3] -= B[i]//(3**m)
                cnt += B[i]//(3**m)
                B[i] -= (B[i]//(3**m))*(3**m)

print(cnt)