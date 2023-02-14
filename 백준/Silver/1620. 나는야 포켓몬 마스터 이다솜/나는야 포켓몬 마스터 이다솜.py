N, M = map(int,input().split())
dict = {}
poke = list(input() for _ in range(N))
for i in range(N):
        input_val = poke[i]
        dict[input_val] = i+1
        
for i in range(M):
       check = input()        
       if check in dict:
               print(dict[check])
       else:
               print(poke[int(check)-1])