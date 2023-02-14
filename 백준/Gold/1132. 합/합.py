N = int(input())

alpha = [0]*10
S = [input() for _ in range(N)]
not_zero = set()

for ap in S:
    not_zero.add(ord(ap[0]) - 65)
    for i in range(len(ap)):
        digit = len(ap) - i - 1
        alpha[ord(ap[i])-65] += 10**digit
        
ans = 0

for n in range(9, -1, -1):
    maxi = 0
    mi = -1
    if len(not_zero) == n: 
        for i in list(not_zero):
            if alpha[i] > maxi:
                mi = i
                maxi = alpha[i]    
    else:        
        for i in range(10):
            if alpha[i] > maxi:
                mi = i
                maxi = alpha[i]
    
    ans += maxi * n
    alpha[mi] = 0
    if mi in not_zero:
        not_zero.remove(mi)
   
print(ans)