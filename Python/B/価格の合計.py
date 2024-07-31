N,X = map(int,input().split())
A = list(map(int,input().split()))
binX = bin(X)
index = -1
indexlist = []
ans = 0

while True:
    if binX[index] == "b":
        break
    elif binX[index] == "1":
        indexlist.append(-index - 1)
    index -= 1

for ind in indexlist:
    ans += A[ind]

print(ans)

        