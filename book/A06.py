N,Q = map(int,input().split())
A = list(map(int,input().split()))
L = []
S = []

for _ in range(Q):
    L.append(list(map(int,input().split())))


S.append(0)

for i in range(1,N+1):
    S.append(S[i-1] + A[i-1]) 

for q in range(Q):
    print(S[L[q][1]] - S[L[q][0]-1])

# print(S)

# print("A:",A)
# print("L:",L)