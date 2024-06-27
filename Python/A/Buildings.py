N = int(input())
H = list(map(int,input().split()))

maxbill = H[0]
ans = -1

for h in range(len(H)):
    if maxbill < H[h]:
        maxbill = max(maxbill,H[h])
        ans = h + 1
        break

print(ans)
