S = input()
score = 4 - (ord(S[0]) - 65)
if score < 0:
    print("0.0")
    exit()
if S[1] == '+':
    score += 0.3
elif S[1] == '-':
    score -= 0.3
print(format(score, ".1f"))