N = int(input())
S = [None] * N
C = [None] * N

for n in range(N):
    S[n],C[n] = input().split()
    C[n] = int(C[n])

S.sort()

print(S[sum(C) %  N])