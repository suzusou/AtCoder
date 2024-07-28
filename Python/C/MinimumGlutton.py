N,X,Y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

Asum = 0
Bsum = 0

Atemp = N
Btemp = N

for n in range(N):
    Asum += A[n]
    if Asum > X:
        Atemp = n + 1
        break

for n in range(N):
    Bsum += B[n]
    if Bsum > Y:
        Btemp = n + 1
        break

if Asum <= X and Bsum <= Y:
    print(N)
    exit()

if Btemp >= Atemp:
    print(Atemp)
else:
    print(Btemp)

        
