N = int(input())
P = list(map(int,input().split()))
Saikyo = P[0]
index = 0

for n in range(N):
    if Saikyo <= P[n]:
        index = n
        Saikyo = P[n]

if index == 0:
    print(0)
else:
    print(Saikyo + 1 - P[0])