N,Q = map(int,input().split())
T = list(map(int,input().split()))
ha = [True] * N

for t in T:
    ha[t-1] = not bool(ha[t-1])

print(ha.count(True))