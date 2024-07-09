N = int(input())
A = list(map(int,input().split()))

for a in range(len(A)):
    if A[a] != A[0]:
        print("No")
        exit()

print("Yes")

    