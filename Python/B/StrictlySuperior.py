N,M = map(int,input().split())
P = []
C = []
F = []

for n in range(N):
    temp = list(map(int,input().split()))
    P.append(temp[0])
    C.append(temp[1])
    F.append(temp[2:])

# print(set([0,1]) <= set([0,2,3]))

for f in range(0,len(F)):
    for i in range(0,len(F)):
        if f != i and (set(F[f]) <= set(F[i]) and P[f] > P[i]) or (set(F[f]) < set(F[i]) and P[f] >= P[i]):
            print("Yes")
            exit()

print("No")
