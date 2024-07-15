N = int(input())
S = [None] * N
A = [None] * N
minnum = 100000000000000000
temp = 0

for n in range(N):
    S[n],A[n] = input().split()
    A[n] = int(A[n])

for n in range(N):
    if A[n] < minnum:
        minnum = A[n]
        temp = n

for i in range(temp,N):
    print(S[i])

for i in range(temp):
    print(S[i])


