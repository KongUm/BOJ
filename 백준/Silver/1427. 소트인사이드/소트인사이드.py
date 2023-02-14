N = input()
count = [0]*10
for i in range(len(N)):
        count[int(N[i])] += 1

for i in range(9,-1,-1):
        for j in range(count[i]):
                print(str(i), end = "")