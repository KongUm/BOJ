K, N = map(int, input().split())
num = []

maxi = 0
for _ in range(K):
    a = input()
    maxi = max(maxi, int(a))
    b = a*(10//len(a))+a[:10%len(a)]
    num.append([int(b), int(a)])
    
c = str(maxi)
d = c*(10//len(c)) + c[:10%len(c)]
for _ in range(N-K):
    num.append([int(d), int(c)])
num.sort(reverse = True)


ans = ""
for i in range(N):
    ans += str(num[i][1])
print(ans)
