N,L = map(int,input().split())
A = list(map(int,input().split()))
ans = 0

for a in A:
    if a >= L:
        ans += 1

print(ans)