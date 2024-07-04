D = int(input())
N = int(input())
LR = []

for  _  in range(N):
    LR.append(list(map(int,input().split())))

B = [0] * (D+2)

for n in range(N):
    B[LR[n][0]] += 1
    B[LR[n][1] + 1] -= 1

ans = [0] * (D+2)

for d in range(1,D+1):
    ans[d] = ans[d-1] + B[d]

for d in range(1,D+1):
    print(ans[d])






