K,G,M = map(int,input().split())

Gml = 0
Mml = 0

for _ in range(K):
    if Gml == G:
        Gml = 0
    elif Mml == 0:
        Mml = M
    else:
        if Mml >= G - Gml:
            temp = G - Gml
            Gml += temp
            Mml -= temp
        else:
            Gml += Mml
            Mml = 0

print(Gml,Mml)

