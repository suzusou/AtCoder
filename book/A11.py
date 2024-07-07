import bisect

N,X = map(int,input().split())
A = list(map(int,input().split()))

# ans = bisect.bisect(A,X)
# print(ans)

L = 0
R = N 

while L <= R:
    M = (L + R) // 2
    if X < A[M]:
        R = M - 1
    elif X == A[M]:
        print(M)
        exit()
    else:
        L = M + 1


