S =input()

a = ""

for i in S:

    if i.isupper():

        a += i.lower()

       

    else:

        a += i.upper()

print(a)

