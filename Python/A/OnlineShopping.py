N,S,K = map(int,input().split())
P = [None] * N
Q = [None] * N

for n in range(N):
    P[n],Q[n] = map(int,input().split())

# print(P)
# print(Q)

total = 0

for n in range(N):
    total += P[n] * Q[n]

if total < S:
    total += K

print(total)