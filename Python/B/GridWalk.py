H,W = map(int,input().split())
Si,Sj = map(int,input().split())

grid = []

for _ in range(H):
    grid.append(list(input()))

X = input()

for x in X:
    if x == "L":
        if Sj > 1 and grid[Si - 1][Sj - 2] == ".":
            Sj -= 1
            grid[Si - 1][Sj - 1] == "#"

    elif x == "R":
        if Sj < W  and grid[Si - 1][Sj] == ".":
            Sj += 1
            grid[Si - 1][Sj - 1] == "#"
    
    elif x == "U":
        if Si > 1 and grid[Si - 2][Sj - 1] == ".":
            Si -= 1
            grid[Si - 1][Sj - 1] == "#"
    
    else:
        if Si < H  and grid[Si][Sj - 1] == ".":
            Si += 1
            grid[Si - 1][Sj - 1] == "#"

print(Si,Sj)