N = int(input())

arr = [[""]*N for _ in range(N)]
S = input()
idx = len(S)-1
for i in range(N):
    for j in range(0, i+1):
        arr[i][j] = S[idx]
        idx -= 1

stack = []
prefix = []

def Check(l):
    for i in range(0, l+1):
        a = prefix[l]
        if i > 0:
            a -= prefix[i-1]
        if (arr[l][i] == '+' and a <= 0) or (arr[l][i] == '-' and a >= 0) or (arr[l][i] == '0' and a != 0):
            return False
    return True


def BT(l):
    if l == N:
        for i in range(N):
            print(stack.pop(), end = " ")
        exit()
    for num in range(-10, 11):
        if len(prefix) > 0:
            prefix.append(prefix[-1] + num)
        else:
            prefix.append(num)
        if Check(l) == False:
            prefix.pop()
            continue
        stack.append(num)
        BT(l+1)
        stack.pop()
        prefix.pop()
BT(0)


