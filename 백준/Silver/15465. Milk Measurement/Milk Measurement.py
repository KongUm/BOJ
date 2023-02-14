N = int(input())
info = [[] for _ in range(101)]
cow = set()

for _ in range(N):
    a, b, c = map(str, input().split())
    info[int(a)].append([b, int(c)])
    cow.add(b)

cow = list(cow)
h_cow = cow[:]
D = {}
for i in range(len(cow)):
    D[cow[i]] = 7
cnt = 0

for i in range(1, 101):
    if len(info[i]) == 0:
        continue
    for name, d in info[i]:
        D[name] += d
    now_max = 0
    temp = []
    for j in D.keys():
        if D[j] > now_max:
            now_max = D[j]
            temp = [j]
        elif D[j] == now_max:
            temp.append(D[j])
    if h_cow != temp:
        cnt += 1
    h_cow = temp[:]
print(cnt)


