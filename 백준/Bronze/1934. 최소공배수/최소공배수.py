T = int(input())

def GCD(a, b): # a > b
  while b != 0:
    temp = b
    b = a % b
    a = temp
  return a

for _ in range(T):
  a, b = map(int, input().split())
  G = GCD(max(a, b), min(a, b))
  LCM = a//G * b//G * G
  print(LCM)
  