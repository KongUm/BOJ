num = [j for j in range(1, 10001)]
k = 1

def d(n):
  a = [int(str(n)[i]) for i in range(len(str(n)))]
  return sum(a) + n

while k <= 10000:
  b = d(k)
  k += 1
  if b > 10000:
    continue
  num[b-1] = 0

for i in range(10000):
  if num[i] != 0:
    print(num[i])
  
  