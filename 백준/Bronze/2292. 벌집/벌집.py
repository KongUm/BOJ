N = int(input())-1
i = 0

if N == 0: print(1)
else:
    while N-6*(i*(i+1)//2) > 0:
        i +=1
    print(i+1)