S = input()
a = len(S)

for i in 'abcdefghijklmnopqrstuvwxyz':
  for j in range(len(S)):
    if S[j] == i:
      print(j, end = ' ')
      break
    if j == len(S)-1:
      print(-1, end = ' ')
      