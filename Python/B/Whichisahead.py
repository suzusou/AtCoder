N = int(input())
P = list(map(int,input().split()))
Q = int(input())

A = [None] * Q
B = [None] * Q

for q in range(Q):
    A[q],B[q] = map(int,input().split())

atemp = 0
btemp = 0

for q in range(Q):
    for p in range(len(P)):
        if A[q] == P[p]:
            atemp = p + 1
        if B[q] == P[p]:
            btemp = p + 1
            
    if atemp < btemp:
        print(A[q])
    else:
        print(B[q])

