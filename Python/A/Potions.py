N,H,X = map(int,input().split())
P = list(map(int,input().split()))
temp = 100000000000000

for p in P:
    if H+p >= X:
        temp = min(temp,p)

for p in range(len(P)):
    if temp == P[p]:
        print(p+1)
        exit()
