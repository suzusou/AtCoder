N = int(input())
A = list(map(int,input().split()))

for a in range(0,len(A)-6,7):
    print(sum(A[a:a+7]),end=" ")
