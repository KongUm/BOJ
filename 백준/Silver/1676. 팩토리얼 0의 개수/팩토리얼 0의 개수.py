import math
N = int(input())
S = str(math.factorial(N))
count = 0
for i in range(len(S)-1,-1,-1):
    if S[i] == "0":
        count += 1
    else:
        break
print(count)