N = int(input())
A = list(map(int,input().split()))
print(*(A[a-1]*A[a] for a in range(1,len(A))),end=" ")
