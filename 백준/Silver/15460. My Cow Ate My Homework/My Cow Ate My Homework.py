import heapq

N = int(input())
A = list(map(int, input().split()))

cnt = [0]*10001
heap = A[:]
heapq.heapify(heap)
for i in A:
    cnt[i] += 1
maxi = 0
ans = []
now_mini = min(A)
S = sum(A)

for i in range(N - 2):
    cnt[A[i]] -= 1
    S -= A[i]
    if cnt[now_mini] == 0:
        while len(heap) > 0:
            a = heapq.heappop(heap)
            if cnt[a] > 0:
                now_mini = a
                heapq.heappush(heap, a)
                break
    t = (S - now_mini) / (N - i - 2)

    if t > maxi:
        maxi = t
        ans = [i + 1]
    elif t == maxi:
        ans.append(i + 1)
for i in ans:
    print(i)




