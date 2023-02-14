from collections import deque

N, K = map(int, input().split())
now = [0] + list(map(int, input().split()))
d = [0] + list(map(int, input().split()))
Q = deque()
s, cnt = [0], [0]

for i in range(1, N + 1):
    c, ss = cnt[-1], s[-1]
    if i - K >= 0:
        c -= cnt[i - K]
        ss -= s[i - K]

    now[i] += (K - i) * c + ss
    if now[i] >= d[i]:
        cnt.append(cnt[-1])
        s.append(s[-1])
        continue

    delta = d[i] - now[i]
    tmp = delta // K
    if (delta % K > 0):
        tmp += 1

    cnt.append(cnt[-1] + tmp)
    s.append(s[-1] + i * tmp)

print(cnt[-1])
