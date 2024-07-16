N,D = map(int,input().split())
T = list(map(int,input().split()))

for n in range(1,N):
    if T[n] - T[n - 1] <= D:
        print(T[n])
        exit()

print(-1)