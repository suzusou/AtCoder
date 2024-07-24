N,T,P = map(int,input().split())
L = list(map(int,input().split()))

L.sort(reverse=True)

print(T - L[P-1] if T - L[P-1] > 0 else 0)