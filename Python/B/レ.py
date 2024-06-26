N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = []
tmp = []

for i in range(1, N + 1):
    tmp.insert(0, i)
    if i not in A:
        ans += tmp
        tmp = []

print(*ans)