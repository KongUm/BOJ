a, b, c = map(int, input().split())
D = int(input()) 

c += D % 60
D = D // 60
if c >= 60:
    c -= 60
    b += 1

b += D % 60
D = D // 60
if b >= 60:
    b -= 60
    a += 1

a += D % 24
if a >= 24:
    a -= 24

print(a,b,c)