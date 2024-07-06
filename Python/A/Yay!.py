S = input()

if S.count(S[0]) >= 2:
    for s in range(1,len(S)):
        if S[s] != S[0]:
            print(s+1)
else:
    print(1)