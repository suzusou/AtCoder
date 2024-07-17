N = int(input())
H = list(map(int,input().split()))
maxnum = max(H)

for n in range(N):
    if H[n] == maxnum:
        print(n + 1)
        exit()