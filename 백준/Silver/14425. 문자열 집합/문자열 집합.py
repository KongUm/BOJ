N, M = map(int,input().split())
S = list(input() for _ in range(N))
C = list(input() for _ in range(M))


dict = {S[i]: True for i in range(len(S))}

count = 0
for i in range(M):
        try:
                if dict[C[i]] == True:
                        count = count + 1
        except:
                continue
                
print(count)