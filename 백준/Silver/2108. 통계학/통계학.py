import sys
N = int(input())

A = [0]*N
count = [0]*8002

for i in range(N):
        input_num = int(sys.stdin.readline())
        A[i] = int(input_num)
        if input_num < 0:
                count[input_num*(-1)] += 1
        else:
                count[input_num+4001] += 1
A.sort()

mode = [0]
count[0] = 0

for i in range(8002):
        if count[i] > count[mode[0]]:
                mode = []
                mode.append(i)
        elif count[i] == count[mode[0]]:
                mode.append(i)
                
        
print(round(sum(A)/N))
print(A[N//2]) #중앙값

for i in range(len(mode)):
        if mode[i] > 4000:
                mode[i] = mode[i] -4001
        else:
                mode[i] = mode[i]*(-1)

if len(mode) > 1:
        mode.remove(min(mode))
        
print(min(mode)) #최빈값

max_num = A[N-1]
min_num = A[0]

print(max_num-min_num) #범위
