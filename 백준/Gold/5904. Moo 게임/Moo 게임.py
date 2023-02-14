N = int(input())

count = 3
level = 0
S = [3]
while count < N:
    level += 1
    count += level+3 + count
    S.append(count)
    
def Search(L):
    global count
    global N
    
    if L == 0:
        return
 
    a = N - S[L-1]
    if a <= 0:
        return Search(L-1)
    elif 1 <= a <= L+3:
        N = a
        return
    else:
        N -= S[L-1] + L+3
        return Search(L-1)
        
Search(level)

if N == 1:
    print("m")
else:
    print("o")