H,W = map(int,input().split())
ans = 0

for _ in range(H):
    ans += input().count("#")

print(ans)
