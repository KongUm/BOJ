n = int(input())
A = [input() for _ in range(n)]

cnt = 0
for i in A:
    if i == "Poblano":
        cnt += 1500
    elif i == "Mirasol":
        cnt += 6000
    elif i == "Serrano":
        cnt += 15500
    elif i == "Cayenne":
        cnt += 40000
    elif i == "Thai":
        cnt += 75000
    else:
        cnt += 125000
print(cnt)