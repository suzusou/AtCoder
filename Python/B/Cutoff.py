N,X = map(int,input().split())
A = list(map(int,input().split()))


for i in range(101):
    A.append(i)
    A.sort()
    if X <= sum(A[1:-1]):
        print(i)
        exit()
    A.remove(i)

print(-1)
        
