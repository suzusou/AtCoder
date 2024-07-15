C1 = list(map(int,input().split()))
C2 = list(map(int,input().split()))

if (C1[5] > C2[2] and C1[4] > C2[1] and C1[3] > C2[0]) and (C2[3] > C1[0] and C2[4] > C1[1] and C2[5] > C1[2]):
    print("Yes")
else:
    print("No")
