A,B,V = map(int, input().split())
N = A-B

if((V-A)%N == 0):
  print((V-A)//N+1)
else:
  print(int((V-A)//N)+2)