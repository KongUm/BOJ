N, new_score, P = map(int, input().split())

if N > 0:
    arr = list(map(int, input().split()))
    arr.append(new_score)
    arr.sort(reverse = True)
    rank = [1]
    for i in range(1,N+1):
        if arr[i] == arr[i-1]:
            rank.append(rank[-1])
        else:
            rank.append(i+1)
        
if N <= 0:
    print(1)
else:
    for i in range(N+1):
        if new_score == arr[i] and (i == N or new_score > arr[i+1]):
            if i+1 > P:
                print(-1)
            else:
                print(rank[i])       
            