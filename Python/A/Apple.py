X,Y,N = map(int,input().split())
Y1 = Y / 3

if Y1 < X:
    Yapple = N // 3
    Xapple = N % 3
    print(Xapple*X + Yapple*Y)
else:
    print(X*N)
