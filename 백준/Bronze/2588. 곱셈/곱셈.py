a = int(input())
b = int(input())

three = a*(b%10)
four = a*((b//10)%10)
five = a*(b//100)
print(three)
print(four)
print(five)
print(five*100+four*10+three)