N = int(input())

alpha = dict()
S = [input() for _ in range(N)]
A = set()

for ap in S:
    for i in range(len(ap)):
        if ap[i] not in A:
            A.add(ap[i])
            alpha[ap[i]] = 0   
            
        digit = len(ap) - i - 1
        alpha[ap[i]] += 10**digit
        
ans = 0

A = list(A)
for n in range(9, -1, -1):
    maxi = 0
    mi = -1
    for i in A:
        if alpha[i] > maxi:
            mi = i
            maxi = alpha[i]
    
    ans += maxi * n
    alpha[mi] = 0
   
print(ans)