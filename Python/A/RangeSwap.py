N,P,Q,R,S = map(int,input().split())
A = list(map(int,input().split()))

temp = A[P-1:Q]
A[P-1:Q] = A[R-1:S]
A[R-1:S] = temp

print(*A)