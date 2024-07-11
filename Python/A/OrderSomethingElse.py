N,P,Q = map(int,input().split())
D = list(map(int,input().split()))
ans = P

for d in D:
    if Q+d <= P:
        ans = min(ans,Q+d)

print(ans)
