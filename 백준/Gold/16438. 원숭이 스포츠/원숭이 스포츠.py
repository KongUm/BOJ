N = int(input())
arr = [[] for _ in range(7)]

def solution(n, value, idx):
    if idx == 7:
        return

    for i in range(n):
        arr[idx].append(value)

    solution(n//2, 0, idx + 1)
    solution(n//2, 1, idx + 1)

solution(64, 0, 0)
solution(64, 1, 0)

for i in range(7):
    if sum(arr[i][:N]) == 128:
        arr[i][0] = 0
    elif sum(arr[i][:N]) == 0:
        arr[i][0] = 1

for i in range(7):
    for j in range(N):
        print(chr(arr[i][j] + 65), end="")
    print()