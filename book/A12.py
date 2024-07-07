N,K = map(int,input().split())
A = list(map(int,input().split()))

L = 1
R = 10 ** 9


while L < R:
    Mid = (L + R) // 2
    total = 0
    for i in range(N):
        total += Mid // A[i]
    if total >= K:
        R = Mid
    else:
        L = Mid + 1


print(L)