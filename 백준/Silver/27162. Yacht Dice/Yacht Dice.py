S = input()
A = list(map(int, input().split()))

cnt = [0] * 7
for i in A:
    cnt[i] += 1
#print(cnt)
a = set(A)
ans = [0]
for i in range(12):   
    if S[i] == 'N':
        continue 
        
    if (i + 1) <= 6:
        ans.append((cnt[i + 1] + 2) * (i + 1))
    
    if (i + 1) == 7:
        for j in range(6, 0, -1):
          
            if cnt[j] >= 2:
                ans.append(j * 4)
             
    
    if (i + 1) == 8:
        if len(a) == 2:
            ans.append(max(A)*3 + min(A) * 2)
        elif len(a) == 1:
            if A[0] == 6:
                ans.append(A[0] * 3 + 10)
            else:
                ans.append(12 + A[0] * 3)
          
            
    if (i + 1) == 9:
        if cnt[6] == 0 and len(a) == 3:
            ans.append(30)
            
    if (i + 1) == 10:
        if cnt[1] == 0 and len(a) == 3:
            ans.append(30)
    
    if (i + 1) == 11:
        if len(a) == 1:
            ans.append(50)
            
    if (i + 1) == 12:
        ans.append(12 + sum(A))
        
print(max(ans))