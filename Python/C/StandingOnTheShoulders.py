N = int(input())
A = [None] * N
B = [None] * N

for n in range(N):
    A[n],B[n] = map(int,input().split())

ans = 0

for n in range(N):
    ans = max(ans,B[n] - A[n])

for n in range(N):
    ans += A[n]

print(ans)
