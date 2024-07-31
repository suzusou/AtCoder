N = int(input())
W = [None] * N
X = [None] * N

for n in range(N):
    W[n],X[n] = map(int,input().split())


ans = 0

for time in range(0,24):
    people = 0
    for n in range(N):
        if 9 <= (time + X[n]) % 24 < 18:
            people += W[n]
    
    ans = max(ans,people)

print(ans)
