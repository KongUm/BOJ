N = int(input())
A = list(map(int, input().split()))
cow = list(map(int, input().split()))

for _ in range(3):
    temp = [0]*N
    for i in range(N):
        temp[i] = cow[A[i] - 1]
    cow = temp[:]

for i in temp:
    print(i)