N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
temp = 0

for a in A:
    temp += a
    if K == temp:
        temp = 0
        ans += 1
    elif K < temp:
        temp = a
        ans += 1

if temp == 0:
    print(ans)
else:
    print(ans + 1)


