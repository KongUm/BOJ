import bisect

N = int(input())
H = list(map(int, input().split()))
comb = []
A = []
for i in range(N):
    for j in range(i+1, N):
        comb.append([H[i] + H[j], i, j])
        A.append(H[i] + H[j])
A.sort()
comb.sort()


mini = int(1e10)

for i in range(len(comb)):
    target = comb[i][0]
    info = [comb[i][1], comb[i][2]]
    
    c = bisect.bisect_left(A, target)
    
    if comb[c][0] == target:
        for j in range(5):
            cx = j + c
            if 0 <= cx < len(comb) and comb[cx][0] == target:
                if comb[cx][1] not in info and comb[cx][2] not in info:
                    print(0)
                    exit()
    
    for j in range(-3,4):
        cx = j + c
        if 0 <= cx < len(comb):
            if comb[cx][1] not in info and comb[cx][2] not in info:
                mini = min(mini, abs(target - comb[cx][0]))

print(mini)
                
        
