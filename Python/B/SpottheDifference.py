N = int(input())
A = []
B = [] 

for _ in range(N):
    A.append(input())

for _ in range(N):
    B.append(input())

# print(A)
# print(B)

for n in range(N):
    if A[n] != B[n]:
        for a in range(N):
            if A[n][a] != B[n][a]:
                print(n + 1,a + 1)
                exit()