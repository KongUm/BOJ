N = int(input())
ans = []

for i in range(N):
    target = N-i
    S = str(target)
    sum_target = 0
    for j in range(len(S)):
        sum_target = sum_target + int(S[j])
    if N-sum_target == target:
        ans.append(target)
        
if len(ans) == 0:
    print(0)
else:
    print(min(ans))