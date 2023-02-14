import math
N, M = map(int,input().split())
A = list(map(int, input().split()))
sum_A = []
mod_A = [0]*M


for i in range(N):
    if i == 0:
        sum_A.append(A[0])
    else:
        sum_A.append(sum_A[i-1]+A[i])
#print(sum_A)

for i in range(N):
    r = sum_A[i]%M
    mod_A[r] += 1
    
ans = mod_A[0]
for i in range(M):
    ans += math.comb(mod_A[i],2)
print(ans)
    
        
