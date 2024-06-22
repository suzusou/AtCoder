import math
import sys
sys.setrecursionlimit(10**9)


def Virus_check(i):
    for j in range(N):
        if Virus[j] == "No" and math.sqrt((zahyou[i][0]-zahyou[j][0])**2 + (zahyou[i][1]-zahyou[j][1])**2) <= D:
            Virus[j] = "Yes"
            Virus_check(j)



N,D = map(int,input().split())
zahyou = []
Virus = {0:"Yes"}

for i in range(N-1):
    Virus[i+1] = "No"


for i in range(N):
    X,Y = map(int,input().split())
    zahyou.append([X,Y])

for i in range(N):
    if Virus[i] == "Yes":
        Virus_check(i)


for i in Virus.values():
    print(i)
