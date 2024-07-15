N,K = map(int,input().split())
A = list(map(int,input().split()))

temp = set()

for n in range(N):
    if A[n] <= K:
        temp.add(A[n])


print(((K * (K + 1)) // 2) - sum(temp))

