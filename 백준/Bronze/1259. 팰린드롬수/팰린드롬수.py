a = ""
while True:
	a = input()
	if a == "0":
		break
	checker = True
	if len(a) == 1:
		checker = True
	elif len(a)%2 == 1:
		for i in range(len(a)//2):
			if a[len(a)//2 -1 - i] != a[len(a) // 2 +1+ i]:
				checker = False
	else:
		for i in range(len(a)//2):
			if a[len(a)//2 + i] != a[(len(a)//2-1) - i]:
				checker = False
	if checker == True:
		print("yes")
	else:
		print("no")