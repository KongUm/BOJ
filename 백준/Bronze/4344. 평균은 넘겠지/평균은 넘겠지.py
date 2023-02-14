C = int(input())
a = [list(map(int, input().split())) for _ in range(C)]

for i in range(C):
  b = 0
  N = (a[i])[0]
  ave = (sum(a[i])-N)/N
  for j in range(1 , N+1):
    if (a[i])[j] > ave:
      b += 1
  ans = b/N*100
  print("{:.3f}%" .format(ans))