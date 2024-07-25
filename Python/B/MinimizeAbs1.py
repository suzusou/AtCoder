N,L,R = map(int,input().split())
A = list(map(int,input().split()))

for a in A:
    if L <= a <= R:
        print(a,end=" ")
    else:
        if abs(a-L) < abs(a-R):
            print(L,end=" ")
        else:
            print(R,end=" ")
