N = int(input())
ABC = list(input() for _ in range(3))
count = 0

for n in range(N):
    if ABC[0][n] != ABC[1][n] and ABC[0][n] != ABC[2][n] and ABC[1][n] != ABC[2][n]:
        count += 2
    elif ABC[0][n] == ABC[1][n] and ABC[0][n] == ABC[2][n] and ABC[1][n] == ABC[2][n]:
        pass
    else:
        count += 1
        
print(count)