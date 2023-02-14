X = int(input())
N = int(input())
ans = 0
    
for i in range(N):
    a,b = input().split()
    a = int(a)
    b = int(b)
        
    ans = ans + a*b
if X == ans:
    print("Yes")
else:
    print("No")