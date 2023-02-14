N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

def BT(index, letter):
        if index > M-1:
                print(letter)
                return
        for i in arr:
                if str(i) not in set(letter.split()):
                        if index == 0:
                                BT(index+1, letter + str(i))
                        else:
                                BT(index+1, letter + " " + str(i))      
BT(0,"") 