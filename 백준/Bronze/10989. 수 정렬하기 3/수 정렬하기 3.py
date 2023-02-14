import sys
N = int(input())

count = [0]*10001

for i in range(N):
        count[int(sys.stdin.readline())] += 1
        
for i in range(1,10000+1):
        if count[i] != 0:
                if i%1000 == 0:
                        sys.stdout.flush()
                for j in range(count[i]):
                        sys.stdout.write(str(i) + "\n")
                        
                        

