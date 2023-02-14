A, B = map(int, input().split())

idc = 1
cnt = [B-A+1]
while True:
    a = A // (2**idc)
    b = B // (2**idc)
    n = b-a
    if A % (2**idc) == 0:
        n += 1
    if n == 0:
        break
    cnt.append(n)
    idc += 1

arr = []
for i in range(len(cnt)-1):
    arr.append(cnt[i] - cnt[i+1])
arr.append(cnt[-1])
score = 0
for i in range(len(arr)):
    score += arr[i]*(2**i)
print(score)