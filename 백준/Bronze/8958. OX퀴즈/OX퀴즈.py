N = int(input())
data = list(input().replace("X", " ").split() for _ in range(N))
a = 0

for i in range(N):
    b = 0
    for j in range(len(data[i])):
        a = len((data[i])[j])
        b = b + a*(a+1)//2
    print(b)