n = int(input())
A = [input() for _ in range(n)]
x = 0; y = 0

for i in A:
    if i == "D":
        x += 1
    else:
        y += 1
    if (abs(x - y) == 2):
        break
print(str(x) + ":" + str(y))