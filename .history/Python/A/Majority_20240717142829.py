N = int(input())

FCount = 0
ACount = 0

for _ in range(N):
    temp = input()
    if temp == "For":
        FCount += 1
    else:
        ACount += 1
if FCount >= ACount:
    print("Yes")
else:
    print("No")


