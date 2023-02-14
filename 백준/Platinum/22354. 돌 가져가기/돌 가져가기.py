N = int(input())

C = input()
A = list(map(int, input().split()))

info = []
a = C[0]
maxi = 0
cnt = 0
for i in range(N):
    if C[i] != a:
        if cnt > 0:
            info.append(maxi)
        cnt += 1
        maxi = 0
        a = C[i]
    maxi = max(maxi, A[i])

info.sort(reverse = True)

if len(info) % 2 == 0:
    count = len(info)//2
else:
    count = (len(info))//2+1
    
ans = 0
for score in info:
    if count == 0:
        break
    ans += score
    count -= 1
print(ans)