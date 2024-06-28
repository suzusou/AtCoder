A = []
count = [0,0,0,0]

for _ in range(3):
    A.append(list(map(int,input().split())))

for i in range(3):
    for j in range(2):
        if A[i][j] == 1:
            count[0] += 1
        elif A[i][j] == 2:
            count[1] += 1
        elif A[i][j] == 3:
            count[2] += 1
        elif A[i][j] == 4:
            count[3] += 1

for c in count:
    if c >= 3:
        print("NO")
        exit()

print("YES")



