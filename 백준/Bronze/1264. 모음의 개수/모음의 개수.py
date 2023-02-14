alpha = ['a', 'e', 'o', 'u', 'i', 'A', 'E', 'O', 'U', 'I']
while True:
    S = input()
    if S == '#':
        exit()
    cnt = 0
    for i in S:
        if i in alpha:
            cnt += 1
    print(cnt)