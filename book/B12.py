# N,K = map(int,input().split())
# A = list(map(int,input().split()))

N = int(input())

L = 0.001
R = 10**6


while L < R:
    Mid = (L + R) / 2
    if Mid**3 + Mid >= N - 0.001 and Mid**3 + Mid <= N + 0.001:
        print(Mid)
        exit()
    elif Mid**3 + Mid <= N - 0.001:
        L = Mid
    else:
        R = Mid


