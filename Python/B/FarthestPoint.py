N = int(input())
X = [None] * N
Y = [None] * N

for n in range(N):
    X[n],Y[n] = map(int,input().split())

for n in range(N):
    temp = []
    
    for m in range(N):
         temp.append((X[n]-X[m])**2 + (Y[n]-Y[m])**2)

    maxnum = max(temp)

    for tmp in range(len(temp)):
        if maxnum == temp[tmp]:
            print(tmp + 1)
            break
    