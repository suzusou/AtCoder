H,W,N = map(int,input().split())
ban = [["."  for _ in range(W)] for _ in range(H)]
Hs = 0
Ws = 0
angle = 0

for _ in range(N):
    if ban[Hs][Ws] == ".":
        angle += 1  
        ban[Hs][Ws] = "#"     
    else:
        angle -= 1 
        ban[Hs][Ws] = "."
         
    if angle % 4 == 1:
        Ws = (Ws + 1) % W
    elif angle % 4 == 2:
        Hs = (Hs + 1) % H
    elif angle % 4 == 3:
        Ws = (Ws - 1) % W
    elif angle % 4 == 0:
        Hs = (Hs - 1) % H 

for h in range(H):
    for w in range(W):
        print(ban[h][w],end="")
    print()



