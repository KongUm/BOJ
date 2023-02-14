N = int(input())
q = N//5
ans = []

def sugar(a):
    if (N-5*a) % 3 == 0:
        return a
    else:
        return -1

for i in range(q+1):
    ans.append(sugar(i))

max_5kg = max(ans)
if max_5kg == -1:
    print(-1)
else:
    print(max_5kg + (N - (max_5kg * 5)) // 3)