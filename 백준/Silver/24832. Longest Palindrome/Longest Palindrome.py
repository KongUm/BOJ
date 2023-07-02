n, m = map(int, input().split())
s = [input() for _ in range(n)]
v1 = []
v2 = []
v3 = []

for i in range(n):
    flag = 1
    for j in range(i + 1, n):
        if (s[i] == s[j][::-1]):
            v1.append(s[i])
            v3.append(s[j])
            flag = 0
            break
    
    if (flag == 1 and s[i] == s[i][::-1]):
        v2.append(s[i])
 
ans = ""
for i in v1:
    ans += i
    
if (len(v2) > 0):
    ans += v2[0]
    
for i in v3[::-1]:
    ans += i
print(len(ans))
print(ans)
            
            