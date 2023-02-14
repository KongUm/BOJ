N = int(input())
ans = []

def find(n,a):
    for i in range(10-a):
        if n == 1:
            ans.append(a)
            ans.append(a*10)
            break
        checker = True
        cur = n
        t = 0
        an = 0
        an2 = 0
        while cur != 0:
            if a+i*t > 9:
                checker = False
                break
            an = an + (a+i*t)*(10**(cur-1))
            an2 = an2 + (a+i*t)*(10**t)
            
            cur = cur - 1
            t = t + 1
        
        if checker == False:
            break
        if a == i:
            ans.append(an2*10)
        
        ans.append(an)
    
        if i != 0:
            ans.append(an2)
leng = len(str(N))

for i in range(1,leng+1):
    for j in range(1,10):
        find(i,j)

out = 0 

for i in ans:
    if i <= N:
    
        out = out + 1
    

print(out)