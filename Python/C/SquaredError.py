from collections import Counter

N = int(input())
A = [*map(int, input().split())]
cnt = Counter(A)
#print(cnt)

ans = 0

for x in range(-200, 201):
    for y in range(x + 1, 201):
        cx = cnt[x]
        cy = cnt[y]
        ans += cx * cy * (x - y) ** 2

print(ans)
