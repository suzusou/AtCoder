N,S,M,L = map(int,input().split())

ans = 1e1000

for s in range(N):
    for m in range(N):
        for l in range(N):
            if s*6 + m*8 + l*12 >= N:
                ans = min(s*S + m*M + l*L,ans)

print(min(S,M,L) if ans == 1e1000 else ans)
            
