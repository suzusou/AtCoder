N,K = map(int,input().split())
ans = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        z = K - i - j
        ans += z >= 1 and z <= N

print(ans)