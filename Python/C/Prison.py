N,M = map(int,input().split())
LR = []
minnum = 0
maxnum = 100001

for _ in range(M):
    LR.append(list(map(int,input().split())))

for m in range(M):
    if LR[m][0] > minnum:
        minnum = LR[m][0]
    if LR[m][1] < maxnum:
        maxnum = LR[m][1]

if maxnum - minnum <= -1:
    print(0)
else:
    print(maxnum - minnum + 1)




