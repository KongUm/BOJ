n = int(input())
s = input()

a = ['a', 'i', 'e', 'o', 'u']

cnt = 0
for i in s:
    if i in a:
        cnt += 1
print(cnt)