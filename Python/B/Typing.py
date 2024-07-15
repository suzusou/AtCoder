S = input()
T = input()

ans = 0
temp = 0

for s in range(len(S)):
    for t in range(len(T)):
        if S[s] == T[t]:
            ans += t + 1
            temp = t
            print(ans,end=" ")
            T = T[temp + 1:]
            break


