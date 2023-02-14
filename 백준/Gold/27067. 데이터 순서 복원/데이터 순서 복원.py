N = int(input())

used = set()

A = [list(map(int, input().split())) for _ in range(3)]

idx = [N - 1, N - 1, N - 1]
stack = []

def most_frequent(data):
    return max(data, key=data.count)

for i in range(N):
    for j in range(3):
        while True:
            if A[j][idx[j]] in used:
                idx[j] -= 1
            else:
                break
    temp = []
    for j in range(3):
        if idx[j] >= 0:
            temp.append(A[j][idx[j]])

    a = most_frequent(temp)
    for j in range(3):
        if idx[j] >= 0:
            if A[j][idx[j]] == a:
                idx[j] -= 1
    stack.append(int(a))
    used.add(a)

for i in range(N):
    print(stack.pop(), end = " ")
