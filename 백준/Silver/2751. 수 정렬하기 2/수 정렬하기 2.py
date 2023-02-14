N = int(input())
num = []
for i in range(N):
        num.append(int(input()))

checker = None
need = False
for i in range(N-1):
        if num[i] >= num[i+1] and (checker == True or checker == None):
                checker = True
        elif num[i] <= num[i+1] and (checker == False or checker == None):
                checker = False
        else:
                need = True
                
if need == True:
        num.sort()
if checker == True and need == False:
        num.reverse()

for i in range(N):
        print(num[i])
        