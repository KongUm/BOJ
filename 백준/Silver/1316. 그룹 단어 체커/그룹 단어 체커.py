N = int(input())
num = 0

for i in range(N):
    a = input()
    b = []
    cur = ""
    for j in range(len(a)):
        if a[j] != cur:
            b.append(a[j])
            cur = a[j]
    c = "".join(set(b))
    if len(b) == len(c):
        num += 1
print(num)