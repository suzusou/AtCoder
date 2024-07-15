N,M = map(int,input().split())
AX = []

for _ in range(N + 1):
    AX.append(list(map(int,input().split())))

# print(AX)

total = 0

for m in range(M):
    for n in range(1,N + 1):
        total += AX[n][m]
    
    # print(total)

    if AX[0][m] > total:
        print("No")
        exit()

    total = 0

print("Yes")

