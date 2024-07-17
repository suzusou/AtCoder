N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0

for b in range(M):
    ans += A[B[b] - 1]

print(ans)
