N,X = map(int,input().split())
P = list(map(int,input().split()))

for n in range(N):
    if P[n] == X:
        print(n + 1)
        exit()