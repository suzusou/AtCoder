import math

N,K = map(int,input().split())
A = list(map(int,input().split()))
X = [None] * N
Y = [None] * N

for n in range(N):
    X[n],Y[n] = map(int,input().split())

Rlist = []
R = []

for n in range(N):
    Rlist = []
    for k in range(K):
        Rlist.append((X[A[k]-1]-X[n])**2 + (Y[A[k]-1]-Y[n])**2)
    R.append(min(Rlist))

print(math.sqrt(max(R)))
