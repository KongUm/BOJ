n = int(input())
A = list(map(int, input().split()))
c = [0, 0]
for i in A:
    if i % 2 == 0:
        c[0] += 1
    else:
        c[1] += 1

if c[0] > c[1]:
    print("Happy")
else:
    print("Sad")