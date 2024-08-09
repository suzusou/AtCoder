S = input()

ans = 1


for ss in range(len(S)):
    for se in range(ss+1,len(S)+1):
        if S[ss:se] == S[ss:se][::-1]:
            ans = max(ans,se-ss)
            
print(ans)
