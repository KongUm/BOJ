N = int(input())
i = 0
j = 0

while N-(i*(i+1)//2) > 0:
    i += 1
while N-((i-1)*i//2)-j > 0:
    j += 1

if i % 2 != 0:
    print("{0}/{1}".format(i-(j-1), 1+(j-1)))
else: print("{0}/{1}".format(1+(j-1), i-(j-1)))