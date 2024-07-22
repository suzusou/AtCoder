S,T = input().split()

for w in range(1,len(S)):
    for st in range(w):
        temp = ""
        for sp in range(st,len(S),w):
            temp += S[sp]
        if temp == T:
            print("Yes")
            exit()

print("No")
