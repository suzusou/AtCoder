N,M = map(int,input().split())
S = [input() for _ in range(N)]



minv = N

for i in range(2**N):
    
    St = set()
    cnt = 0
    for j in range(N):
        # iが0～255、jが0～7
        # iのjビット目が1かどうかをチェックします
        if i & (1 << j):
            print("i",i)
            cnt += 1
            for l in range(M):
                if S[j][l] == 'o':
                    St.add(l)
    
    if len(St) == M:
        minv = min(minv, cnt)

print(minv)

# print(2 & (1 << 2))

# if 2 & (1 << 2):
#     print("Condition is true")
# else:
#     print("Condition is false")
