N,M,X = map(int,input().split())
A = list(map(int,input().split()))
temp = 0

for a in range(len(A)):
    if a == len(A)-1:
        break

    if A[a] < X and A[a+1] > X:
        temp = a + 1
        break

print(min(temp,len(A)-temp))