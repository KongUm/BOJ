L = int(input())
S = input()

hash = 0

for i in range(L):
    hash = hash + (ord(S[i])-96)*(31**i)
print(hash)