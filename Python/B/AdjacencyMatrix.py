N = int(input())
A = []

for n in range(N):
    A.append(list(map(int,input().split())))

for n in range(N):
    for m in range(N):
        if A[n][m] == 1:
            print(m + 1,end=" ")
    print()
