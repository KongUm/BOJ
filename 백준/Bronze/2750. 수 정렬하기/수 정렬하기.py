N = int(input())
num = []
for i in range(N):
        num.append(int(input()))

for i in range(N):
        for j in range(N-i-1):
                if num[j] > num[j+1]:
                        temp = num[j]
                        num[j] = num[j+1]
                        num[j+1] = temp
                        
for i in range(N):
        print(num[i])