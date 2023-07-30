T = int(input())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for _ in range(T):
    k, m = map(int, input().split())
    x = 0; y = 0
    A = [[] for _ in range(4)]
    B = [[] for _ in range(4)]
    
    now = 1
    
    for i in range(12):
        A[i % 4].append((now - 1) % 9 + 1)
        now *= m
        
    for i in range(12):
        B[i % 4].append((now - 1) % 9 + 1)
        now *= m
    
    if (k >= 12):
        x = sum(A[1]) - sum(A[3])
        y = sum(A[0]) - sum(A[2])
    else:
        for i in range(4):
            cnt = (k - 1) // 4 + (((k - 1) % 4) >= i)
            y += sum(A[i][:(cnt % 3)]) * dy[i]
            x += sum(A[i][:(cnt % 3)]) * dx[i]  
            
    k -= 12 
    
    if (k > 0):
        for i in range(4):
            cnt = (k - 1) // 4 + (((k - 1) % 4) >= i)
            y += (sum(B[i]) * (cnt // 3) + sum(B[i][:(cnt % 3)])) * dy[i]
            x += (sum(B[i]) * (cnt // 3) + sum(B[i][:(cnt % 3)])) * dx[i]
    print(x, y)
    
    
        
    
    