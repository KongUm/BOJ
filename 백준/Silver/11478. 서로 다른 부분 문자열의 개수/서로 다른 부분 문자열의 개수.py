S = input()
ans = []

for i in range(1,len(S)+1): #부분문자열의 길이
      
      if len(S) == i:
              ans.append(S)
      else:
              for j in range(len(S)-i+1): #부분문자열 시작지점 설정
                      ans.append(S[j:j+i])
print(len(set(ans)))
