# N日間、1日周遊パスD枚セット、P円
# i日　Fi円の料金がかかる

N,D,P = map(int,input().split())
F = list(map(int,input().split()))
F.sort(reverse=True)
ans = 0
temp = len(F)


for f in range(0,len(F),D):
    #リスト外に出そうなとき
    if f+D > len(F)-1:
        if sum(F[f:len(F)]) > P:
            ans += P  
        else:
            temp = f
            break
    else:
        if sum(F[f:f+D]) > P:
            ans += P  
        else:
            temp = f
            break

ans += sum(F[temp:len(F)])
print(ans)

