S = input()
ans = ""

for s in range(0,len(S) - 1,2):
    ans += S[s + 1]
    ans += S[s]

print(ans)
