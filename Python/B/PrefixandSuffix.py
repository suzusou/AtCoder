N,M = map(int,input().split())
S = input()
T = input()

if S == T[0:N] and S == T[M-N:M]:
    print(0)
elif S == T[0:N] and S != T[M-N:M]:
    print(1)
elif S != T[0:N] and S == T[M-N:M]:
    print(2)
else:
    print(3)
