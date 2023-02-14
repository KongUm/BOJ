N = list(map(int, input().split()))
ascend = 0
descend = 0

for i in range(8):
    if N[i] == i+1:
        ascend = ascend + 1
    elif N[i] == 8-i:
        descend = descend + 1
        
    
if ascend == 8:
    print("ascending")
elif descend == 8:
    print("descending")
else:
    print("mixed")
