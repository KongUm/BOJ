N = int(input())
S = input()
cnt = 0

for i in S:
    if i == 's':
        cnt += 1
se, bi = cnt, N - cnt

if se == bi:
    print("bigdata? security!")
elif se > bi:
    print("security!")
else:
    print("bigdata?")