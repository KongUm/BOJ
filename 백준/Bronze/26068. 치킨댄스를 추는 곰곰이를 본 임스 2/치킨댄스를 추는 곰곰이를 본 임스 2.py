N = int(input())

cnt = 0
for _ in range(N):
    S = input()
    if int(S[2:]) <= 90:
        cnt += 1
print(cnt)