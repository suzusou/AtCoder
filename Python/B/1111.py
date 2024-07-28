N = int(input())
D = list(map(int,input().split()))
ans = 0

for n in range(1,N + 1):
    if n < 10:
        if 10*n + n <= D[n - 1]:
            ans += 2
        elif n <= D[n - 1]:
            ans += 1
    elif n % 11 == 0:
        if n <= D[n - 1]:
            ans += 2
        elif n % 10 <= D[n - 1]:
            ans += 1


print(ans)
        

