N,A,B = map(int,input().split())
C = list(map(int,input().split()))

for n in range(N):
    if C[n] == A + B:
        print(n + 1)
        exit()